
from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('addauthor/', views.add_author, name='add_author'),
    path('addrecipe/', views.add_recipe, name='add_recipe'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logout_view, name='logout')
]
