from django.urls import path

from . import views

app_name = 'restaurants'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),  # edite esta linha
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'), # adicione esta linha
    path('search/', views.search_posts, name='search'), # adicione esta linha
    path('create/', views.PostCreateView.as_view(), name='create'), # adicione esta linha
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories<int:pk>', views.CategoryDetailView.as_view(), name='detail-category'),
]