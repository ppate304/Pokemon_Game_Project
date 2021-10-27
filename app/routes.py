from flask import Flask, render_template, request
import requests 
from app import app
from .forms import LoginForm
from .forms import PokimonForm

@app.route('/home')
def home():
    return render_template('home.html.j2')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get("email").lower()
        password = request.form.get("password")
        if email in app.config.get("REGISTERED_USERS") and \
            password == app.config.get("REGISTERED_USERS").get(email).get('password'):
            return f"Login success Welcome {app.config.get('REGISTERED_USERS').get(email).get('name')}"
        error_string = "Invalid Email password combo"
        return render_template('login.html.j2', error = error_string, form=form)
    return render_template('/login.html.j2', form=form)

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