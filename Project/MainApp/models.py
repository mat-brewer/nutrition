from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date


class Food(models.Model):
    name = models.CharField(max_length=100, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serving_size_g = models.DecimalField(default=100, max_digits=5, decimal_places=1)
    protein = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    total_fats = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    saturated_fats = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    mono_unsaturated_fats = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    poly_unsaturated_fats = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    total_carbohydrates = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    energy = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    sugars = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    fiber = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    calcium = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    iron = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    magnesium = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    potassium = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    sodium = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    vitamin_c = models.DecimalField(default=0, max_digits=5, decimal_places=1)


    class Meta:
        '''Limits the user from making duplicates of food'''
        unique_together = ('name', 'user', 'protein', 'total_fats', 'total_carbohydrates', 'energy', 'sugars', 'fiber', 'calcium', 
                           'iron', 'magnesium', 'potassium', 'sodium', 'vitamin_c', 'saturated_fats', 'mono_unsaturated_fats', 'poly_unsaturated_fats',)
        ordering = ['name']


    @property
    def calories(self):
        return round(((self.protein*4) + (self.total_carbohydrates*4) + (self.total_fats*9)), 1)


    def __str__(self):
        return f'{self.name} | {self.calories} cal | {self.serving_size_g}g'.capitalize()



class Meal(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foods = models.ManyToManyField(Food)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return f'{self.name} | {self.total_calories} calories'.capitalize()


    @property
    def total_calories(self):
        list_of_calories = []
        for food in self.foods.all():
            list_of_calories.append(float(food.calories))
        return sum(list_of_calories)


    @property
    def total_protein(self):
        total_proteins_list = []
        for food in self.foods.all():
            total_proteins_list.append(food.protein)
        proteins = sum(total_proteins_list)*(food.serving_size_g/100)
        return proteins


    @property
    def total_fats(self):
        total_fats_list = []
        for food in self.foods.all():
            total_fats_list.append(food.total_fats)
        fats = sum(total_fats_list)
        return fats


    @property
    def total_carbs(self):
        total_carbs_list = []
        for food in self.foods.all():
            total_carbs_list.append(food.total_carbohydrates)
        carbs = sum(total_carbs_list)
        return carbs


    @property
    def macro_total(self):
        return f'Protein: {self.total_protein} Fats: {self.total_fats} Carbs: {self.total_carbs}'


class Day(models.Model):
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meals = models.ManyToManyField(Meal)
    notes = models.CharField(max_length=140, null=True, blank=True)

    class Meta:
        '''Limits the user from making multiple entries for the same day'''
        unique_together = ('date', 'user')
    

    @property
    def is_today(self):
        today = date.today()
        format = today.isoformat()
        if str(self.date) == format:
            return True
        else:
            return False


    @property
    def total_calories(self):
        total = 0
        for meal in self.meals.all():
            total += meal.total_calories
        return f'Calories: {total}'


    @property
    def total_protein(self):
        total_proteins_list = []
        for meal in self.meals.all():
            total_proteins_list.append(meal.total_protein)
        proteins = sum(total_proteins_list)
        return proteins


    @property
    def total_fats(self):
        total_fats_list = []
        for meal in self.meals.all():
            total_fats_list.append(meal.total_fats)
        fats = sum(total_fats_list)
        return fats


    @property
    def total_carbs(self):
        total_carbs_list = []
        for meal in self.meals.all():
            total_carbs_list.append(meal.total_carbs)
        carbs = sum(total_carbs_list)
        return carbs


    @property
    def macro_total(self):
        return f'Protein: {self.total_protein} Fats: {self.total_fats} Carbs: {self.total_carbs}'

    @property
    def micro_total(self):
        pass


    @property
    def avg_calories_day(self):
        pass


    def __str__(self):
        date = str(self.date)
        return date
