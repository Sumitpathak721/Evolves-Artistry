from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home,name='home'),
    path('home/',views.Home,name='home'),
    path('Creater/',views.Creater,name='Creater'),
    path('Blogs/',views.Blogs,name='Blog'),
    path('Blogs/<str:blog_name>/',views.Blog,name="Detail_of_blog")
]
