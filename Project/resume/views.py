from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def home_mat(request):
    return render(request, 'resume/portfolio.html', {'test_context':'context info here'})


#def home(request):
#    context = {
#        'posts': Post.objects.all()
#    }
#    return render(request, 'blog/home.html', context)