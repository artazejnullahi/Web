from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),  # ✅ Correct URL for Projects
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),  # ✅ Fix for the 'about' error

    

]
