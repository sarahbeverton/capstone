from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from boards.models import Board
from boards.forms import BoardForm
from pinusers.models import PinUser
from pins.models import Pin
# Create your views here.


class AddBoardView(LoginRequiredMixin, View):
    form_class = BoardForm

    def get(self, request):
        html = "board_form.html"
        form = self.form_class()
        context = {'form': form}
        return render(request, html, context)

    def post(self, request):
        post_data = request.POST
        form = self.form_class(post_data)
        if form.is_valid():
            data = form.cleaned_data
            current_user = PinUser.objects.get(username=request.user.username)
            my_board = Board.objects.create(
                title=data['title'],
                description=data['description'],
                user=current_user
            )
            return redirect("profile", username=request.user.username)


class BoardView(LoginRequiredMixin, View):
    def get(self, request, board_id):
        my_board = Board.objects.get(id=board_id)
        board_pins = my_board.pins.values()
        html = "board_detail.html"
        context = {'board': my_board, 'board_pins': board_pins}
        return render(request, html, context)


class SaveToBoardView(LoginRequiredMixin, View):
    def get(self, request, pin_id, board_id):
        current_user = PinUser.objects.get(username=request.user.username)
        my_pin = Pin.objects.get(id=pin_id)
        my_board = Board.objects.get(id=board_id)
        my_board.pins.add(my_pin)
        current_user.pins.add(my_pin)
        return redirect("profile", username=request.user.username)
