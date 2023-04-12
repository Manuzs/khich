from khichdiapp import db

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique = True, nullable = False)
    image_file = db.Column(db.String(30), default = 'default.jpg')
    ingredients = db.Column(db.Text ,nullable = False)
    recipe = db.Column(db.Text(), nullable = False)
    entree_name = db.Column(db.String(30), default = 'Anon')

    def __repr__(self) :
        return f"Recipes('{self.recipe_name}','{self.ingredients}', '{self.recipe}','{self.entree_name}', '{self.image_file}')"



