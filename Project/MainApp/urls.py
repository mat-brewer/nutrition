from django.urls import path, register_converter
from datetime import datetime
from . import views

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')


urlpatterns = [
    path('', views.main, name='home'),
    path('dashboard/', views.DashboardMainView.as_view(), name='dashboard'),
    path('about/', views.about, name='about'),
    # food urls
    path('food/create/', views.FoodCreateView.as_view(), name='food-create'),
    path('food/view/<str:user>/<int:pk>/<str:name>', views.FoodDetailView.as_view(), name='food-view'),
    path('food/<int:pk>/update/', views.FoodUpdateView.as_view(), name='food-update'),
    path('food/<int:pk>/delete/', views.FoodDeleteView.as_view(), name='food-delete'),
    # meal urls
    path('meal/create/', views.MealCreateView.as_view(), name='meal-create'),
    path('meal/view/<str:user>/<int:pk>/<str:name>', views.MealDetailView.as_view(), name='meal-view'),
    path('meal/<int:pk>/update/', views.MealUpdateView.as_view(), name='meal-update'),
    path('meal/<int:pk>/delete/', views.MealDeleteView.as_view(), name='meal-delete'),
    # day urls
    path('day/view/<str:user>/<int:pk>/<yyyy:date>', views.DayDetailView.as_view(), name='day-view'),
    path('day/create/', views.DayCreateView.as_view(), name='day-create'),
    path('day/<int:pk>/update/', views.DayUpdateView.as_view(), name='day-update'),
    path('day/<int:pk>/delete/', views.DayDeleteView.as_view(), name='day-delete'),
]

# python manage.py runserver