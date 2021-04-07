from django.urls import path
from . views import (ArticleListView,ArticleUpdateView, # new
    ArticleDetailView, # new
    ArticleDeleteView,
    CreateNewArticle,
    #home,
)

urlpatterns = [
    #path("", home),
    path('', ArticleListView.as_view(), name='article_list'),
    path('edit/<int:pk>/',
         ArticleUpdateView.as_view(), name='article_edit'), # new
    path('<int:pk>/',
         ArticleDetailView.as_view(), name='article_detail'), # new
    path('delete/<int:pk>/',
         ArticleDeleteView.as_view(), name='article_delete'),
    path('new-article/',
         CreateNewArticle.as_view(), name='create_article'),
]