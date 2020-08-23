from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.
from .form import LoginForm


def login_demo(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['user_name'], password=cd['passwd'])
            if user:
                login(request, user)
                return render(request, 'success.html')
            else:
                return render(request, 'fail.html', {'form': login_form})
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})
