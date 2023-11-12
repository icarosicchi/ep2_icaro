from django.http import HttpResponse
from .temp_data import movie_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.shortcuts import render, get_object_or_404


def list_movies(request):
    movie_list = Post.objects.all()
    context = {'movie_list': movie_list}
    return render(request, 'restaurants/index.html', context)

def detail_movie(request, movie_id):
    post = get_object_or_404(Post, pk=movie_id)
    context = {'post': post}
    return render(request, 'restaurants/detail.html', context)

def search_movies(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        movie_list = Post.objects.filter(title__icontains=search_term)
        context = {"movie_list": movie_list}
    return render(request, 'restaurants/search.html', context)

def create_movie(request):
    if request.method == 'POST':
        post_name = request.POST['title']
        post_content = request.POST['content']
        post_poster_url = request.POST['poster_url']
        post = Post(title=post_name,
                      content=post_content,
                      poster_url=post_poster_url)
        post.save()
        return HttpResponseRedirect(
            reverse('restaurants:detail', args=(post.id, )))
    else:
        return render(request, 'restaurants/create.html', {})
    
def update_movie(request, movie_id):
    post = get_object_or_404(Post, pk=movie_id)

    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post_poster_url = request.POST['poster_url']
        post.save()
        return HttpResponseRedirect(
            reverse('restaurants:detail', args=(post.id, )))

    context = {'post': post}
    return render(request, 'restaurants/update.html', context)


def delete_movie(request, movie_id):
    post = get_object_or_404(Post, pk=movie_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('restaurants:index'))

    context = {'post': post}
    return render(request, 'restaurants/delete.html', context)