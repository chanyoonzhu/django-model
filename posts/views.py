from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomeView(ListView): # List view for our posts
    
    model = Post # add model to View

    template_name = "home.html"

    context_object_name = "all_posts" # use customized "object_list"

class PostDetailView(DetailView):
    
    model = Post

    template_name = "post_detail.html"

