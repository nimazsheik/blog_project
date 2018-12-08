from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) ### replace usercreationform with userregister form the one we made
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
            #display the flash messages in base.html (check it)
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
