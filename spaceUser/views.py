from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from .form import PasswordResetConfirmForm, RegisterForm, LoginForm
from homepage.forms import SearchForm
from spaceUser.models import User


def register(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            context = {}
            return render(request, 'spaceUser.html', context)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def identification(request):
    form_search = SearchForm()
    form = LoginForm()
    if request.method == "POST":
        password = request.POST['password']
        email = request.POST['email']
        user = authenticate(request, email=email,
                            password=password,)
        if user is not None:
            login(request, user)
            context = {"last_name": user.last_name,
                       "email": user.email, 'form_search': form_search}
            return render(request, 'spaceUser.html', context)
        else:
            message = "Utilisateur ou mot de passe incorrect"
            return render(request, 'login.html', {
                'form': form,
                'form_search': form_search,
                "message": message})
    return render(request, 'login.html', {
        'form': form, 'form_search': form_search})


@login_required
def spaceUser(request):
    form_search = SearchForm()
    user = User.objects.get(id=request.user.id)
    context = {'form_search': form_search, 'user': user}
    return render(request, 'spaceUser.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')

def password_reset(request):
    password_reset = PasswordResetView()
    if request.method == "POST":
        form = password_reset.form_class
        if form.is_valid():
            form.save()
            form.send_mail()
            context={'form':form}
            return render(request, 'password_reset_form.html', context)

def password_reset_done(request):
    template = PasswordResetCompleteView()
    context = {'template':template.template_name}
    return render(request, 'password_reset_done.html', context)

def password_reset_confirm(request):
    passwordResetConfirm = PasswordResetConfirmForm()
    if request.method == "POST":
        form = PasswordResetConfirmForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            context = {'template':passwordResetConfirm.template_name}
            return render(request, 'password_reset_confirm.html', context)

def password_reset_succes(request):
    template = PasswordResetConfirmView()
    context = {'template':template.template_name}
    return render(request, 'password_reset_succes.html', context)