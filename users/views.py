from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LogoutView as BaseLogoutView, PasswordChangeView as BasePasswordChangeView,
    PasswordResetDoneView as BasePasswordResetDoneView, PasswordResetConfirmView as BasePasswordResetConfirmView,
)
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.utils.crypto import get_random_string
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import View, FormView
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django import forms

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)               
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, _('Successfull logged in'))
            return redirect('/')           
        else:
            # Return an 'invalid login' error message.
            messages.info(request, _('Please, fill form'))
            
            
    else:
        messages.info(request, _('Going to login page'))   
        
    
    return render(request, 'login.html')
    

@login_required(login_url='login.html')    
def Dashboard(request):
    username = request.user
    context={'user': username}
    return render(request, 'dsh.html', context)    
   
   
def logout_view(request):
    logout(request)
    
    
    return render(request,'logout.html')    