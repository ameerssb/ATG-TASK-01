from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('doctor/login/', views.D_Login.as_view(),name='DLogin'),
    path('doctor/register', views.D_Register.as_view(),name='DRegister'),
    path('patient/login/', views.P_Login.as_view(),name='PLogin'),
    path('patient/register/', views.P_Register.as_view(),name='PRegister'), 
    path('logout/', LogoutView.as_view(next_page='Home'), name='Logout'),
    path('add_blog/', views.Blog_Post, name='add_blog'),    
]
