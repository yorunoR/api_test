from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    making_time = models.CharField(max_length=100)
    serves = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)
    cost = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "recipes"
        verbose_name = "レシピ"
        verbose_name_plural = "レシピ"
