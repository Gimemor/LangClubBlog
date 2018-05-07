from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post


# Create your views here.
def index(request):
    # Retrieve all the posts from the user's this person is following.
    posts = Post.objects.all()
    # This will render the posts.
    return render(request, 'post.html', {'posts': posts})


