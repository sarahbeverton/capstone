from django.shortcuts import render, reverse, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from pins.models import Pin
from boards.models import Board
from pinusers.models import PinUser
from pins.forms import PinForm

# Create your views here.

class PinView(View):
    def get(self, request, pin_id):
        my_pin = Pin.objects.get(id=pin_id)
        current_user = PinUser.objects.get(username=request.user.username)
        user_boards = Board.objects.filter(user=current_user)
        html = "pin_detail.html"
        context = {'pin': my_pin, 'boards': user_boards}
        return render(request, html, context)


class SaveView(LoginRequiredMixin, View):
    def get(self, request, pin_id):
        my_pin = Pin.objects.get(id=pin_id)
        request.user.pins.add(my_pin)
        return redirect("profile")


class AddPinView(LoginRequiredMixin, View):
    form_class = PinForm

    def get(self, request):
        html = "pin_form.html"
        form = self.form_class()
        context = {'form': form}
        return render(request, html, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            my_pin = Pin.objects.create(
                title=data['title'],
                description=data['description'],
                photo=data['photo'],
                url=data['url'],
            )
            my_pin.save()
            # will change below to profile page once that url is created
            return redirect("homepage")
        # need to add error 400, 500 handling
