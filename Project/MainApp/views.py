from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (
    ListView, 
    TemplateView, 
    DetailView,
    CreateView, 
    UpdateView, 
    DeleteView)
from .services import search_food
from .models import Food, Meal, Day
from .forms import MealForm, DayForm


def main(request):
    '''function to display the apps home page'''
    # makes dashboard the home page for logged in users
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    else:
        return render(request, 'MainApp/home_page.html')



def about(request):
    '''function to display the apps about page'''
    return render(request, 'MainApp/about.html')


class DashboardMainView(LoginRequiredMixin, ListView):
    '''Dashboard view. Passes Days and user.foods to context'''
    #context_object_name = 'days'
    template_name = 'MainApp/dashboard_main.html'
    queryset = Day.objects.all()


    # to pass multiple models into the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foods'] = Food.objects.filter(user=self.request.user)
        context['days'] = Day.objects.filter(user=self.request.user)
        context['meals'] = Meal.objects.filter(user=self.request.user)
        return context


# all things for Food
class GetFood(LoginRequiredMixin, TemplateView):
    '''Gets data from FDC api through search_food function which has a user search query passed in as an argument.'''
    template_name = 'MainApp/search.html'


    def get_context_data(self, **kwargs):
        print(self.request.GET)
    # checks if there is a search_query in the request
        context = super().get_context_data(**kwargs)
        if 'search_query' in self.request.GET:
            query = self.request.GET['search_query']
            context = search_food(query) # receives returned var 'food' from services and stores into context
            return context
        else:
            query = False
            return context


class FoodDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    '''uses generic DetailView to display Food. Login is required to view. test_func validates the current user'''
    model = Food


    def test_func(self):
        food = self.get_object()
        if self.request.user == food.user:
            return True
        else:
            return False


class FoodCreateView(LoginRequiredMixin, CreateView):
    '''uses generic CreateView to create Food. Login is required to use. form_valid validates the current user and form submission'''
    # looks for template called food_form.html
    model = Food
    fields = ['name', 'energy', 'protein', 'total_fats', 'saturated_fats', 'mono_unsaturated_fats', 'poly_unsaturated_fats', 'total_carbohydrates', 
              'sugars', 'fiber', 'calcium', 'iron', 'magnesium', 'potassium', 'sodium', 'vitamin_c' ]
    success_url = '/dashboard/'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FoodUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''uses generic UpdateView to update Food. Login is required to use. form_valid and test_func validate the current user and form submission'''
    model = Food
    fields = ['name', 'energy', 'protein', 'total_fats', 'saturated_fats', 'mono_unsaturated_fats', 'poly_unsaturated_fats', 'total_carbohydrates', 
              'sugars', 'fiber', 'calcium', 'iron', 'magnesium', 'potassium', 'sodium', 'vitamin_c' ]


    # validates form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    def test_func(self):
        food = self.get_object()
        if self.request.user == food.user:
            return True
        else:
            return False


class FoodDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''uses generic DeleteView to display and deletion of Day. Login is required to view. test_func validates the current user'''
    model = Food
    success_url = '/dashboard/'


    def test_func(self):
        day = self.get_object()
        if self.request.user == day.user:
            return True
        else:
            return False


# all things for Meal
class MealDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    '''uses generic DetailView to display Meal. Login is required to view. test_func validates the current user'''
    model = Meal


    def test_func(self):
        meal = self.get_object()
        if self.request.user == meal.user:
            return True
        else:
            return False


class MealCreateView(LoginRequiredMixin, CreateView):
    '''uses generic CreateView to create Meal. Login is required to use. form_valid validates the current user and form submission'''
    model = Meal
    success_url = '/dashboard/'
    form_class = MealForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MealUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''uses generic UpdateView to update Meal. Login is required to use. form_valid and test_func validate the current user and form submission'''
    model = Meal
    success_url = '/dashboard/'
    form_class = MealForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


    # validates form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    def test_func(self):
        meal = self.get_object()
        if self.request.user == meal.user:
            return True
        else:
            return False


class MealDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''uses generic DeleteView to display and deletion of Day. Login is required to view. test_func validates the current user'''
    model = Meal
    success_url = '/dashboard/'


    def test_func(self):
        day = self.get_object()
        if self.request.user == day.user:
            return True
        else:
            return False


# all things for Day
class DayDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    '''uses generic DetailView to display Day. Login is required to view. test_func validates the current user'''
    model = Day


    def test_func(self):
        day = self.get_object()
        if self.request.user == day.user:
            return True
        else:
            return False


class DayCreateView(LoginRequiredMixin, CreateView):
    '''uses generic CreateView to create Day. Login is required to use. form_valid validates the current user and form submission'''
    model = Day
    success_url = '/dashboard/'
    form_class = DayForm


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DayUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''uses generic UpdateView to update Day. Login is required to use. form_valid and test_func validate the current user and form submission'''
    model = Day
    success_url = '/dashboard/'
    form_class = DayForm


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


    # validates form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    def test_func(self):
        day = self.get_object()
        if self.request.user == day.user:
            return True
        else:
            return False


class DayDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''uses generic DeleteView to display and deletion of Day. Login is required to view. test_func validates the current user'''
    model = Day
    success_url = '/dashboard/'


    def test_func(self):
        day = self.get_object()
        if self.request.user == day.user:
            return True
        else:
            return False