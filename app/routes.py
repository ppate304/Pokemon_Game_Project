from flask import render_template, request, redirect, url_for
import requests
from werkzeug.security import check_password_hash 
from app import app
from .forms import LoginForm, RegisterForm
from .forms import PokimonForm
from .models import User
from flask_login import login_user, current_user, logout_user, login_required
@app.route('/home')
def home():
    return render_template('home.html.j2')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get("email").lower()
        password = request.form.get("password")
        u =User.query.filter_by(email=email).first()

        if u and u.check_password_hash(password):
            login_user(u)
            return redirect(url_for('home'))
        error_string = "Invalid Email password combo"
        return render_template('login.html.j2', error = error_string, form=form)
    return render_template('/login.html.j2', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:

            new_user_data = {
                "first_name":form.first_name.data.title(),
                "last_name":form.last_name.data.title(),
                "email":form.email.data.lower(),
                "password":form.password.data
        }
            new_user_object = User()
            new_user_object.from_dict(new_user_data)
            new_user_object.save()

        except:
            error_string = "There was an error"
            return render_template('register.html.j2', form=form, error= error_string)
        return redirect(url_for('login'))
    return render_template('register.html.j2', form=form)

@app.route('/pokimon', methods=['GET', 'POST'])
def pokimon():
    form = PokimonForm()
    if request.method == 'POST':
        name = request.form.get('name')
        print(name)
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        if response.ok:
            if not response.json():
                return "We had an error loading your data likely the year or round is not in the database"
            data = response.json()
            poki_name = []
            print(data)
            poki_dict={}
            poki_dict['Name'] = data['forms'][0]['name']
            poki_dict['abilities'] = data['abilities'][0]['ability']['name']
            poki_dict['base_experience'] = data['base_experience']
            poki_dict['sprite'] = data['sprites']['front_shiny']
            poki_dict['hp'] = data['stats'][0]['base_stat']
            poki_dict['attack'] = data['stats'][1]['base_stat']
            poki_dict['defense'] = data['stats'][2]['base_stat']   
            poki_name.append(poki_dict) 
            print(poki_name)
            return render_template('/pokimon.html.j2', pokis=poki_name, form=form)

        else:
            return "We had a problem"
    
    return render_template('pokimon.html.j2', form=form)