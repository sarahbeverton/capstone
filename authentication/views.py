from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import logout, login, authenticate
from django.db.models import Q

from authentication.forms import LoginForm, SignUpForm
from pinusers.models import PinUser
from pins.models import Pin

# Create your views here.

class IndexView(View):
    def get(self, request):
        search_pin = request.GET.get('search')

        if search_pin:
            pins = Pin.objects.filter(Q(title__icontains=search_pin) | 
                                      Q(description__icontains=search_pin))
        else:
            pins = Pin.objects.all().order_by('-created_at')
     
        html = "index.html"
        context = {'pins': pins}
        return render(request, html, context)


class SignUpView(View):
    form_class = SignUpForm
    html = "signup_form.html"
    context = {}

    def get(self, request):
        form = SignUpForm()
        return render(request, "signup_form.html", {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = PinUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )
            return HttpResponseRedirect(reverse("homepage"))

        return render(request, "signup_form.html", {'form': form})


class LogInView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login_form.html", {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password'],
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))


class LogOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))


def error_view(request, exception):
    return render('404.html')


def server_error_view(request):
    return render('500.html')
