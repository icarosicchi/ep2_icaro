from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm


def list_posts(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'restaurants/index.html', context)

def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'restaurants/detail.html', context)

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(title__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'restaurants/search.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_title = form.cleaned_data['title']
            post_content = form.cleaned_data['content']
            post_poster_url = form.cleaned_data['poster_url']
            post = Post(title=post_title,
                          content=post_content,
                          poster_url=post_poster_url)
            post.save()
            return HttpResponseRedirect(
                reverse('restaurants:detail', args=(post.id, )))
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'restaurants/create.html', context)

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.poster_url = form.cleaned_data['poster_url']
            post.save()
            return HttpResponseRedirect(
                reverse('restaurants:detail', args=(post.id, )))
    else:
        form = PostForm(
            initial={
                'title': post.title,
                'content': post.content,
                'poster_url': post.poster_url
            })

    context = {'post': post, 'form': form}
    return render(request, 'restaurants/update.html', context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('restaurants:index'))

    context = {'post': post}
    return render(request, 'restaurants/delete.html', context)