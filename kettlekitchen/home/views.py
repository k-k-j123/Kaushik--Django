from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Recipe, DefaultRecipe
from .forms import RecipeForm

def index(request):
    return render(request, 'login.html')

@login_required
def home(request):
    default_recipes = DefaultRecipe.objects.all()
    return render(request, 'home.html', {'recipes': default_recipes})

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.publisher = request.user
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'create_recipe.html', {'form': form})

@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id, publisher=request.user)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  # Redirect to home page after login.
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')

def registerUser(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'register.html')

def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, publisher=request.user)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')  # Redirect to a suitable URL after deletion
    return render(request, 'confirm_delete.html', {'recipe': recipe})

def user_recipes(request):
    user_recipes = Recipe.objects.filter(publisher=request.user)
    return render(request, 'user_recipes.html', {'recipes': user_recipes})

def about(request):
    return render(request,'About.html')

def default_recipes(request):
    default_recipes = DefaultRecipe.objects.all()
    return render(request, 'home.html', {'default_recipes': default_recipes})

def default_recipe_detail(request, default_recipe_id):
    default_recipe = get_object_or_404(DefaultRecipe, pk=default_recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': default_recipe})
