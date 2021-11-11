from .import bp as social
from flask import render_template, flash, redirect, url_for, request
from app.models import Pokemon, User
from flask_login import login_required, current_user

@social.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        name=request.form.get('name')
        new_pokemon=Pokemon(user_id=current_user.id, name=name)
        new_pokemon.save()
        return redirect(url_for('social.index'))
    pokemon=current_user.pokemon()
    return render_template('home.html.j2', pokemon=pokemon)

@social.route('/show_users')
@login_required
def show_users():
    users = User.query.all()
    return render_template('show_users.html.j2', users = users)
    
    
@social.route('/poki_attack/<int:id>')
@login_required
def poki_attack(id):
    user_to_attack = User.query.get(id)
    flash(f"You just attacked {user_to_attack.first_name}", 'success')
    if current_user.poki_attack(user_to_attack):
        flash(f"You just won against {user_to_attack.first_name}", 'success')  
        return redirect(url_for('social.show_users'))
    else:
        flash(f"You lost to  {user_to_attack.first_name}", 'warning')
        return redirect(url_for('social.show_users'))

@social.route('/show_points')
@login_required
def show_points():
    poki_points = User.query.all()
    current_user.poki_points(poki_points)
    return render_template('show_points.html.j2', users = poki_points)

