from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),  # Added register URL here
    path('home/', views.home, name='home'),
    path('create-recipe/', views.create_recipe, name='create_recipe'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/delete/', views.delete_recipe, name='delete_recipe'),
    path('user-recipes/', views.user_recipes, name='user_recipes'),
    path('about/',views.about,name='about'),
    path('default_recipes/<int:default_recipe_id>/', views.default_recipe_detail, name='default_recipes'),
    path('default_recipes/', views.default_recipes, name='default_recipes'),

]
