from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

class Recipe(models.Model):
    NOVICE = 1
    BEGINNER = 2
    COMPETENT = 3
    PRO = 4
    EXPERT = 5

    LEVELS = [
        (NOVICE, 'Novice'),
        (BEGINNER, 'Beginner'),
        (COMPETENT, 'Competent'),
        (PRO, 'Pro'),
        (EXPERT, 'Expert'),
    ]
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)

class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.IntegerField()