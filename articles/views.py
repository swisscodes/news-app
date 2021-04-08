from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.urls import reverse_lazy # new
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

#def home(request):
    #return render(request, template_name = 'home.html')
    # articles/views.py




class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = "all_articles"


class ArticleDetailView(DetailView): # new
    model = Article
    template_name = 'article_detail.html'
    context_object_name = "this_article"


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    context_object_name = "this_article"
    success_url = reverse_lazy('article_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    context_object_name = "this_article"
    success_url = reverse_lazy('article_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user
        
    
class CreateNewArticle(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'newarticle.html'
    fields = ('title', 'body')
    success_url = reverse_lazy('article_list')
    
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
    
