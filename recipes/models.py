from django.core.validators import DecimalValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

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
    level = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])

class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.IntegerField()