from django import forms
from .models import Food, Meal, Day

class MealForm(forms.ModelForm):

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foods'].queryset = Food.objects.filter(user=user)

    class Meta:
        model = Meal
        fields = ['name', 'foods']


class DayForm(forms.ModelForm):

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['meals'].queryset = Meal.objects.filter(user=user)

    class Meta:
        model = Day
        fields = ['date', 'meals', 'notes']
