from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordForm, UserInfoForm
from django.db.models import Q
from payment.forms import ShippingForm
from payment.models import ShippingAddress
import json
from Cart.cart import Cart

# Create your views here.[

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']

        searched = Product.objects.filter(Q(name__icontains = searched) | Q(description__icontains = searched) | Q(price__icontains = searched))
        # | MEANS OR
        #icontains is a field lookup that is used to perform case-insensitive containment tests. It checks if a specified substring exists within a given string field in a database query.
        return render(request, 'search.html', {'searched': searched})
    else:
        return render(request, 'search.html', {})
        if not searched:
            messages.success(request, ("No Matching Products Found!!"))

        


    


def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id = request.user.id)
        #Get shipping info of user
        shipping_user = ShippingAddress.objects.filter(id = request.user.id).first()
        #Get Original Usser Form
        form = UserInfoForm(request.POST or None, instance = current_user)
        #Get Shipping Form
        shipping_form = ShippingForm(request.POST or None, instance = shipping_user)
        return render(request, 'update_info.html', {'form': form, 'shipping_form': shipping_form})

        if form.is_valid() or shipping_form.is_valid():
            #save original information
            form.save()
            #save shipping information
            shippinf_form.save()
            messages.success(request, "Your Information has been Updated!!")
            return redirect('home')
    else:
        messages.success(request, "You must be Logged in to access this page!!")
        return redirect('home')
    

    

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = UpdatePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "User Account Password Updated!!")
                #login(request, current_user)
                return redirect('login')
                
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
        else:
            form = UpdatePasswordForm(current_user)
            return render(request, 'update_password.html', {'form': form})
        
    else:
        messages.success(request, "User Account Password Updated!!")
    
    


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id = request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance = current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "User Account Updated!!")
            return redirect('home')
        return render(request, 'update_user.html', {'user_form': user_form})
    else:
        messages.success(request, "You must be Logged in to access this page!!")
        return redirect('home')

    

def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories": categories})

def category(request, foo):
    try: 
        category = Category.objects.get(name = foo)
        products = Product.objects.filter(category = category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, ("This Category does not exist"))
        return redirect('home')


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {'product': product})

def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {'products': products})

def about(request):
    return render(request, "about.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            #Do some shopping
            current_user = Profile.objects.get(user__id = request.user.id)
            #Get their saved cart from database
            saved_cart = current_user.old_cart
            if saved_cart:
                 #Convert database string to dictionary
                converted_cart = json.loads(saved_cart)
                #Add the loaded cart to our session
                #Get the cart
                cart = Cart(request)
                #Loop through the cart and add the items from the database
                for key, value in converted_cart.items():
                    cart.db_add(product = key, quantity = value)

            messages.success(request, ("You Have Been Logged In!....."))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please try again!"))
            return redirect('login')


    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out!!"))
    return redirect('login')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have Registered your Account!!"))
            #send them to update info page after successful registration
            return redirect("update_info")
        else:
            messages.success(request, ("There was an error, please try again!"))
            return redirect("register")
        
    else:
        return render(request, 'register.html', {'form':form})
