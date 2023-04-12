from flask import render_template, flash, redirect, url_for
from khichdiapp import app,db
from khichdiapp.forms import RecipeForm
from khichdiapp.models import Recipes
import random


recipes = [
    [0, 'Khichdi', "heres how to make - it"],
    [1, 'Khichdi', "heres how to make - it"],
    [2, 'Khichdi', "heres how to make - it"],
    [3, 'Khichdi', "heres how to make - it"],
    [4, 'Khichdi', "heres how to make - it"],
    [5, 'Khichdi', "heres how to make - it"],
    [6, 'Khichdi', "heres how to make - it"],
    [7, 'Khichdi', "heres how to make - it"],
]



@app.route('/')
@app.route('/home')
def home():
    x = Recipes.query.count()
    n = len(recipes)
    rnum = random.randint(1, n)
    rnum2 = random.randint(1, x+1)
    rec = Recipes.query.filter_by(id = 2)
    return render_template('home.html', rnum = rnum, recipes = recipes, recs = rec )


@app.route('/contribute', methods = ['GET', 'POST'])
def contribute():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipes(recipe_name = form.recipe_name.data, image_file = form.picture.data,ingredients = form.ingredients.data, recipe = form.recipe.data, entree_name = form.entree_name.data)
        db.session.add(recipe)
        db.session.commit()
        flash("Your recipe updated",'success')
        return render_template('contribute.html', form = form)
    return render_template('contribute.html', form = form)