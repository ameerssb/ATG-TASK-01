from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from account.models import Blog
from account.forms import BlogForm
# Create your views here.
class Home(View):
    def get(self,request):
        context = {}
        return render(request, "home.html", context)


@login_required(login_url='/account/patient/login')
def Dashboard(request):
    blog = Blog.objects.all()
    posts = Blog.objects.exclude(status='Draft')
    form = BlogForm()
    context = {'blog':blog,'posts':posts,'form':form}
    return render(request, 'dashboard.html',context)