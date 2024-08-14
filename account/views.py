from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib import messages
from .forms import LoginForm,RegisterForm,BlogForm
from django.views import View
from .models import User,Blog

# Create your views here.
class D_Login(View):
    def get(self,request):
        context = {'name':'Doctor'}
        return render(request, "account/login.html", context)

    def post(self,request):
        data = request.POST
        print(data)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('dashboard')  # Redirect to Home or dashboard
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('DLogin')
        else:
            messages.error(request, 'Invalid form submission')
            return redirect('DLogin')
            
class D_Register(View):
    def get(self,request):
        context = {'name':'Doctor'}
        return render(request, "account/register.html", context)

    def post(self,request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():            
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('DLogin')
        else:
            print(form.error_messages)
            messages.error(request, form.error_messages)
            return redirect('DRegister')
        
class P_Login(View):
    def get(self,request):
        context = {'name':'Patient'}
        return render(request, "account/login.html", context)

    def post(self,request):
        data = request.POST
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('dashboard')  # Redirect to Home or dashboard
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('DLogin')
        else:
            messages.error(request, 'Invalid form submission')
            return redirect('DLogin')

class P_Register(View):
    def get(self,request):
        context = {'name':'Patient'}
        return render(request, "account/register.html", context)
        
        
    def post(self,request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():            
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('PLogin')
        else:
            print(form.error_messages)
            messages.error(request, form.error_messages)
            return redirect('PRegister')

def Blog_Post(request):
    if request.method == 'POST':
        if request.user.status == 'Doctor':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': True, 'message': 'Blog post created successfully.'})
            else:
                print(form.errors)
                return JsonResponse({'success': False, 'errors': form.errors})