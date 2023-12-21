from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as authLogin

def login(request):
    erro = False
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('login')
            password = request.POST.get('senha')
            user = authenticate(username=username, password=password)
            if user:
                authLogin(request, user)
                return redirect('index')
            else:
                erro = True
    context = {'form': form, 'erro': erro}
    return render(request, 'users/login.html', context)


