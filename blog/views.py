from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def top(request):
    return render(request, "blog/top.html", {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/post_list.html", {'posts':posts})

def report(request):
    # Create "Post form"
    return render(request, "blog/report.html", {})

def login(request):
    # Create "login form"
    return render(request, "blog/login.html", {})