from django.shortcuts import render,HttpResponse

from .models import admin_data,admin_blog
from project1.settings import BASE_DIR
# Create your views here.

def Home(request):
    if admin_data.objects.all():
        return render(request,'index.html',{'page_name':'Home','all_data':reversed(list(admin_data.objects.all()))})
    else:
        return HttpResponse("<h1>No Data Found</h1>")
def Blogs(request):
    if admin_blog.objects.all():
        return render(request,'blogs.html',{'title':'Blog','page_name':"Blog",'blogs':reversed(list(admin_blog.objects.all()))})
    else:
        return HttpResponse("<h1>No Data Found</h1>")
def Creater(request):
    return render(request,'creater.html',{'title':'Creater','page_name':'Creater',})
def Blog(request,blog_name):
    for i in admin_blog.objects.all():
        if str(i)==blog_name:
            return render(request,'blog.html',{'blog_name':i})
    
    return HttpResponse("{{blog_name.images}}Blog file not exist")