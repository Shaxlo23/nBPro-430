from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import get_user_model,login,logout,authenticate
from django.contrib.auth.decorators import login_required


from . import models
from .forms import RegisterForm,LoginForm

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

#     O'ZM QILDMMMMMMMMMMMM

#   HOME 
def home_view(request):
    users = User.objects.all()
    return render(request, 'home_view.html',{'users': users})


#  REGISTER
def register_view(request):

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            user = form.save()

            #  AUTO LOGIN

            login(request,user)

            return redirect('home_view')
        
    return render(request,'register.html', {'form':form})


#     LOGIN

def login_view(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(
            request,
            data = request.POST
        )        


        if form.is_valid():

            email = form.cleaned_data.get('username')

            password = form.cleaned_data.get('password')

            user = authenticate(
                request,
                email = email,
                password = password
            )

            if user is not None:

                login(request,user)

                return redirect('home_view')
            
    context = {
        'form' : form
    }

    return render(
        request, 'login.html',context
    )

#     LOGOUTTT

def logout_view(request):

    logout(request)

    return redirect('login')



@login_required
def profile_view(request):
    context = {
        'user': request.user
    }

    return render(request,'profile.html',context)