"""Blogly application."""

from flask import Flask, render_template, jsonify, request, session, url_for, redirect, abort, flash
from dotenv import load_dotenv
from models import db, connect_db, User   
from routes_posts import posts_bp
from routes_users import users_bp 
# from flask_sqlalchemy import SQLAlchemy

load_dotenv('.flaskenv')

app = Flask(__name__, template_folder='../templates', static_folder='../static') 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bloglydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = "sesh_secr"

with app.app_context():
    connect_db(app)
    db.create_all()
    
# with app.app_context():
#     db.init_app(app)
#     connect_db(app)
#     db.create_all()
# db = SQLAlchemy(app)
# connect_db(app)
# db.create_all()

app.register_blueprint(users_bp)
app.register_blueprint(posts_bp)

# connect_db(app)
# db.create_all() 



# @app.route('/')
# def home():
#     return redirect('/users')

# @app.route('/users')
# def list_users():
#     users = User.query.all()
#     return render_template('list.html', users=users)

# @app.route('/users/new')
# def new_user():
#     return render_template('create.html') 

# @app.route('/users/new', methods=['POST'])
# def add_user():
#     first_name = request.form['first_name'].strip() or "No"
#     middle_name = request.form['middle_name'] or ""
#     last_name = request.form['last_name'].strip() or "Name"
#     image_url = request.form['image_url']
#     new_user = User(first_name=first_name, middle_name=middle_name, last_name=last_name, image_url=image_url)
#     db.session.add(new_user)
#     db.session.commit()
#     return redirect('/users')

# @app.route('/users/<int:user_id>')
# def show_user(user_id):
#     user = User.query.get_or_404(user_id)
#     return render_template('details.html', user=user) 

# @app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
# def edit_user(user_id):
#     user = User.query.get_or_404(user_id)
    
#     if request.method == 'POST':
#         user.first_name = request.form['first_name']
#         user.middle_name = request.form['middle_name']
#         user.last_name = request.form['last_name']
#         user.image_url = request.form['image_url']
#         db.session.commit()
#         flash(f"{user.first_name} {user.middle_name} {user.last_name} updated!")
#         return redirect(url_for('show_user', user_id=user.id))
        
#     return render_template('edit.html', user=user)

# @app.route('/users/<int:user_id>/delete', methods=['POST'])
# def delete_user(user_id):
#     user = User.query.get_or_404(user_id)
#     db.session.delete(user)
#     db.session.commit()
#     return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)