from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html',{})   
    else:
        return render(request, 'login.html',{})
    

def login_user(request):
    if request.method == 'POST':
        uNmae = request.POST['uName']
        pWord = request.POST['pWord']

        user = authenticate(request, username=uNmae, password=pWord)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been login!")
            return redirect('home')            
        else:
            messages.success(request,"Wrong Credentials!")
            return render(request, 'login.html',{})
    else:
        return render(request, 'login.html',{})

   
    
def mainPage(request):
    return render(request, 'home.html',{})


def logout_user(request):
    messages.success(request,"You logout successfully")
    logout(request)
    return render(request, 'logout.html',{})
   