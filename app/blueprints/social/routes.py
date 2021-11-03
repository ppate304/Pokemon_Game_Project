from .import bp as social
from flask import render_template, flash, redirect, url_for, request
from app.models import Post
from flask_login import login_required, current_user

# @social.route('/home', methods = ['GET', 'POST'])
# @login_required
# def home():
#     if request.method == 'POST':
#         name=request.form.get('name')
#         new_post=Post(user_id=current_user.id, name=name)
#         new_post.save()
#         return redirect(url_for('social.index'))
#     posts=current_user.followed_posts()
#     return render_template('home.html.j2', posts=posts)

# @social.route('/show_users')
# @login_required
# def show_users():
#     users = Post.query.all()
#     return render_template('show_pokis.html.j2', users = users)


