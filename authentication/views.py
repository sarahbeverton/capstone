from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import logout, login, authenticate
from authentication.forms import LoginForm, SignUpForm
from pinusers.models import PinUser
# Create your views here.


class IndexView(View):
    def get(self, request):
        html = "index.html"
        context = {}
        return render(request, html, context)

class SignUpView(View):
    form_class = SignUpForm
    html = "generic_form.html"
    context = {}

    def get(self, request):
        form = SignUpForm()
        return render(request, "generic_form.html", {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = PinUser.objects.create(
                username=data['username'],
                password=data['password'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )
            return HttpResponseRedirect('/success/')

        return render(request, "generic_form.html", {'form': form})


class LogInView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "generic_form.html", {'form': form})

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
                return HttpResponseRedirect(request.GET.get('next', reverse("home")))


class LogOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("loginview"))
