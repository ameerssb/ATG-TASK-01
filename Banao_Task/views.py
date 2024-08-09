from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.
class Home(View):
    def get(self,request):
        context = {}
        return render(request, "home.html", context)


@login_required(login_url='/account/patient/login')
def Dashboard(request):
    return render(request, 'dashboard.html')