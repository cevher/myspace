from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin #extended class 
from django.contrib.auth.decorators import login_required #decorator
from django.utils import timezone
from django.urls import reverse_lazy
from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment

# Create your views here.
class AboutView(TemplateView):
    template_name= 'about.html'


class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class CreatePostView(CreateView, LoginRequiredMixin):
    #auth mixin/decorator used to limit access to login users
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post  


class PostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post  


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url ='/login/'
    redirect_field_name= 'blog/post_list.html'
    model = Post

    def get_queryset(self):
       return Post.objects.filter(published_date__isnull=True).order_by('created_date') # not published posts
       