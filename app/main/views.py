from flask_login import login_required, current_user
from flask import render_template, request, redirect, url_for,abort,flash
from . import main
from .. import db
from ..models import User,Pitch,Comment,Category,Vote,Upvotes,Downvotes
from .forms import UpdateProfile, UploadPitch, LikeForm,DislikeForm, CommentForm

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
        # category = form.category.data 
        # pitch = form.pitch.data 
        # username = form.username.data

        # cat=Category.query.filter_by(catname =category).first()
        # uzer= User.query.filter_by(username = username).first()

        new_pitch = Pitch (pitchword = form.pitch.data, category=form.category.data, user = current_user)
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('.viewpitch'))
    return render_template('addpitch.html',upload_form=form)
    
# @main.route('/viewpitch/comment/<int:pitch_id>')
# def addcomment(pitch_id):

    




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


@main.route('/comment', methods=['GET','POST'])
def comment(pitch_id):
    pitch = Pitch.query.filter_by(id =pitch_id)
        
    form = CommentForm()
    if form.validate_on_submit:
        new_comment = Comment(commentword = form.comment.data, pitch_id=pitch.id, user_id=current_user.id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.comment',pitch_id=pitch_id))

    return render_template('comments.html', comment_form=form,pitchcomments=pitch, pitch_id=pitch_id)

@main.route('/business')
def business():
    business_pitches = Pitch.query.filter_by(catname_id=1).all()

    title= "Business Pitches"

    return render_template('business.html', title=title, business_pitches=business_pitches)

@main.route('/auditions')
def auditions():
    auditions_pitches = Pitch.query.filter_by(catname_id=2).all()

    title= "Auditions Pitches"

    return render_template('auditions.html', title=title, auditions_pitches=auditions_pitches)

@main.route('/interviews')
def interviews():
    interviews_pitches = Pitch.query.filter_by(catname_id=3).all()

    title= "Interview Pitches"

    return render_template('interviews.html', title=title, interviews_pitches=interviews_pitches)

@main.route('/pickups')
def pickups():
    pickups_pitches = Pitch.query.filter_by(catname_id=4).all()

    title= "Pick Up Line Pitches"

    return render_template('pickups.html', title=title, pickups_pitches=pickups_pitches)    




