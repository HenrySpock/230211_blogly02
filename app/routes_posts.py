from flask import Blueprint 
from flask import Flask, render_template, jsonify, request, session, url_for, redirect, abort, flash
from dotenv import load_dotenv

from models import Post, User
from models import db

# posts_bp = Blueprint('posts', __name__)

#Routes are called @posts_bp. instead of @app. 
# Alright, time for post routes:

# First, the titles of all posts will be listed as links next to the
# associated user on list.html.  

# Now we need our routes:
# GET /users/[user-id]/posts/new 
#     Show form to add a post for that user new_post.html. 
# POST /users/[user-id]/posts/new 
#     Handle add form; add post and redirect to the user details.html page.
# GET /posts/[post-id] 
#     Show a post.html page with the title, content and created at datetime of the post, and 3 buttons: return to user's page, edit post and delete post. 
# GET /posts/[post-id]/edit 
#     Show form to edit a post edit_post.html which can edit title and/or content of post, with buttons to cancel (redirect to post.html page) or save the edit.
# POST /posts/[post-id]/edit 
#     Handle saving the post edit. Redirect back to the post.html view page.
# POST /posts/[post-id]/delete
#     Delete the post, redirect to the user's details.html page.

# Can you provide updated routes_posts.py, list.html, new_post.html, post.html, and edit_post.html? Is there anything I'm overlooking?

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

@posts_bp.route('/<int:user_id>/new')
def new_post_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('new_post.html', user=user)

@posts_bp.route('/<int:user_id>/new', methods=['POST'])
def new_post(user_id):
    title = request.form.get('title')
    content = request.form.get('content')
    user = User.query.get_or_404(user_id)

    if title:
        post = Post(title=title, content=content, user=user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('users.show_user', user_id=user.id))
    else:
        return render_template('new_post.html', user=user, error="Title is required.")

@posts_bp.route('/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@posts_bp.route('/<int:post_id>/edit')
def edit_post_form(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('edit_post.html', post=post)

@posts_bp.route('/<int:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    title = request.form.get('title')
    content = request.form.get('content')

    if title:
        post.title = title
        post.content = content
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts.show_post', post_id=post.id))
    else:
        return render_template('edit_post.html', post=post, error="Title is required.")

@posts_bp.route('/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('users.show_user', user_id=post.user_id))