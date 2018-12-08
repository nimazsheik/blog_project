from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # replace usercreationform with userregister form the one we made
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are able to login!')
            return redirect('login')
            # display the flash messages in base.html (check it)
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


#django will look in default login route location
#so need to change in settings.py
@login_required
def profile(request):
    return render(request, 'users/profile.html')