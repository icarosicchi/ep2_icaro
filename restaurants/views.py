from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.views import generic
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostListView(generic.ListView):
    model = Post
    template_name = 'restaurants/index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'restaurants/detail.html'

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(title__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'restaurants/search.html', context)

class PostCreateView(generic.CreateView):
    model = Post
    fields = ["title", "content", "poster_url"]
    template_name = 'restaurants/create.html'
    success_url = reverse_lazy('restaurants:index')

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = ["title", "content", "poster_url"]
    template_name = 'restaurants/update.html'
    success_url = reverse_lazy('restaurants:index')

class PostDeleteView(generic.DeleteView):
    model = Post
    fields = ["title", "content", "poster_url"]
    template_name = 'restaurants/delete.html'
    success_url = reverse_lazy('restaurants:index')

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('restaurants:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'restaurants/comment.html', context)    