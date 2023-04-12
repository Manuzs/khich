from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    picture = FileField('Add recipe picture', validators=[FileAllowed(['jpeg', 'png','jpg'])])
    recipe = TextAreaField('Add Recipe', validators=[DataRequired()])
    submit = SubmitField('Submit')
    entree_name = StringField('Your name')
    



