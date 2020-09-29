from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired
from ..models import Category,Pitch,Comment,User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [InputRequired()])
    submit = SubmitField('Submit')

def category_query():
    return Category.query 

class UploadPitch(FlaskForm):
    category = QuerySelectField(query_factory= category_query, allow_blank = True)
    pitch = TextAreaField("Enter your pitch", validators =[InputRequired()])
    username = StringField("Insert your username", validators = [InputRequired()])
    submit = SubmitField("Submit")

class LikeForm(FlaskForm):
    like=SubmitField("Upvote")

class DislikeForm(FlaskForm):
    dislike=SubmitField("DownVote")

class CommentForm(FlaskForm):
    comment = TextAreaField("Your comment", validators =[InputRequired()])
    submit = SubmitField("Submit")






  