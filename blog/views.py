from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator

PAGE_SIZE = 4

# Create your views here.
def index(request):
    # Retrieve all the posts from the user's this person is following.
    allposts = Post.objects.all()
    paginator = Paginator(allposts, PAGE_SIZE)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # This will render the posts.
    return render(request, 'post.html', {'posts': posts})


