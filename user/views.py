from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import get_user_model
from . import models
# Create your views here.

User = get_user_model()

#read
def users_view(request):
    users = User.objects.all()
    return render(request,'users_view.html',context={'users':users})

def user_view(request,slug):
    user = get_object_or_404(User,slug=slug)
    return render(request,'user_view.html',{'user':user})


#create
def user_create(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        avatar = request.FILES.get('avatar')
        phone_number = request.POST.get('phone_number')

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            avatar=avatar,
            phone_number=phone_number,
        )

        return redirect('/')
    return render(request,'user_create.html')

#update
def user_update(request,slug):
    user = get_object_or_404(User,slug=slug)

    if request.method=='POST':
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.email=request.POST.get ('email')
        user.avatar=request.FILES.get('avatar')
        user.phone_number=request.POST.get('phone_number')
        user.save()

        return redirect(f'/user/{user.slug}')
    
    return render(request,'user_update.html',{'user':user})


#delete
def user_delete(request,slug):
    user = get_object_or_404(User,slug=slug)
    if request.method=='POST':
        user.delete()

        return redirect('/')
    return render(request,'user_delete.html',{'user': user})
    