from django.shortcuts import render, reverse, redirect
from django.views.generic import View

from pins.models import Pin

# Create your views here.

class PinView(View):
    def get(self, request, pin_id):
        my_pin = Pin.objects.get(id=pin_id)
        html = "pin_detail.html"
        context = {'pin': my_pin}
        return render(request, html, context)


class SaveView(View):
    def get(self, request, pin_id):
        my_pin = Pin.objects.get(id=pin_id)
        request.user.pins.add(my_pin)
        return redirect("profile")
