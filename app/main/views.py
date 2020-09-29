from flask_login import login_required
from flask import render_template, request, redirect, url_for,abort,flash
from . import main
from .. import db
from ..models import User,Pitch,Comment,Category,Vote,Upvotes,Downvotes
from .forms import UpdateProfile, UploadPitch, LikeForm,DislikeForm

@main.route('/')
def index():
    
    title = "Pitch Up"
    return render_template('index.html', title = title)

@main.route('/showpitch')
def showpitch():
    pitch_examples = Pitch.query.all()

    title = "Sample Pitches"
    return render_template('showpitch.html', title = title, pitch_examples=pitch_examples)

@main.route('/viewpitch',methods=['GET','POST'])
def viewpitch():
    pitch_examples = Pitch.query.all()
    # t=0
    # like_form = LikeForm()
    # if like_form.validate_on_submit:
    #     t +=1
    #     flash("Your vote has been recorded")
    #     return p=str(t)
    # else:
    #     pass
    # dislike_form = DislikeForm()
    # if dislike_form.validate_on_submit:
    #     t +=1
    #     flash("Your vote has been recorded")
    #     return p=str(t)
    # else:
    #     pass

    title = "Pitches"
    return render_template('viewpitch.html',title = title,pitch_examples=pitch_examples)

@main.route('/uploadpitch', methods=['GET','POST'])
def uploadpitch():
    form = UploadPitch()
    if form.validate_on_submit():
        category = form.category.data 
        pitch = form.pitch.data 
        username = form.username.id
        new_pitch = Pitch(pitchword=pitch,category=category,user=username)

        db.session.add(new_pitch)
        db.session.commit()
    return render_template('addpitch.html',upload_form=form)
    
    




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    
    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>/addpitch', methods = ['GET','POST'])
@login_required
def upload_pitch(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UploadPitch()
    if form.validate_on_submit():
        category = form.category.data 
        pitch = form.pitch.data 
        username = form.username.id
        new_pitch = Pitch(pitchword=pitch,category=category,user=username)
        db.session.add(new_pitch)
        db.session.commit()
        
