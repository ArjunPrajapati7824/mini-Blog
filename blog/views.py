from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.contrib import messages
from django.contrib.auth.models import *


from .models import blog_post 
from .forms import *
#Create your views here.

#home
def home(request):
    fm=blog_post.objects.all()
    return render(request,'home.html',{"form":fm})

#about
def about(request):
    return render(request,'about.html')

#contact
def contact(request):
    return render(request,'contact.html')


#dashboard
def dashboard(request):
    if request.user.is_authenticated:
        form=blog_post.objects.all()
        user=request.user
        name=user.get_full_name()
        gps=user.groups.all()
        return render(request,'dashboard.html',{"form":form,"name":name,"gps":gps})
    else:
        return redirect(reverse_lazy('login'))
        
        

#signup
def signup(request):
    if request.method == "POST":
        fm=signupform(request.POST)
        if fm.is_valid():
            messages.success(request,"now u can log in")
            user=fm.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
            return redirect(reverse_lazy('login'))
        else:
            return redirect(reverse_lazy('signup'))
    else:
        fm=signupform()   
    return render(request,'signup.html',{"form":fm})

#login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm=loginform(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"you logged in successfully")
                    return redirect(reverse_lazy('dashboard'))
                else:
                    messages.error(request,"wrong")
                    
                    return redirect(reverse_lazy('login'))
        else:
            fm=loginform(request.user)
        return render(request,'login.html',{"form":fm})
    else:
        return redirect(reverse_lazy('dashboard'))
        
        


#logout
def user_logout(request):
    logout(request)
    return redirect(reverse_lazy('home'))



#add post 
def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form=adddata(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                data=blog_post(title=title,desc=desc)
                data.save()
                return redirect(reverse_lazy('dashboard'))

        else:
            form=adddata()  
        return render(request,'addpost.html',{"form":form})
    else:
        return redirect(reverse_lazy('login'))
    
    
#update post 
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi=blog_post.objects.get(pk=id)
            form=adddata(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                return redirect(reverse_lazy('dashboard'))
        else:
            
            pi=blog_post.objects.get(pk=id)
            form=adddata(instance=pi)
        return render(request,'updatepost.html',{"form":form})    
    else:
        return redirect(reverse_lazy('login'))



def delete(request,id):
    if request.user.is_authenticated:    
        fm=blog_post.objects.get(pk=id)
        fm.delete()
        return redirect(reverse_lazy('dashboard'))
    else:
        return redirect(reverse_lazy('login '))
        