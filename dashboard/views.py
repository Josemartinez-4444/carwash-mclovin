from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home(request):

    if not request.user.is_authenticated:
        return redirect('/login')

    return render(request, 'base.html')


def login_view(request):

    error = ""

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            error = "Usuario o contraseña incorrectos"

    return render(request, 'login.html', {
        'error': error
    })