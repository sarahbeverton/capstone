from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import View

from boards.models import Board
from boards.forms import BoardForm
from pinusers.models import PinUser
from pins.models import Pin
# Create your views here.


class AddBoardView(View):
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
            # will change below to profile page once that url is created
            return HttpResponseRedirect(reverse("homepage"))
        # need to add error 400, 500 handling


class BoardView(View):
    def get(self, request, board_id):
        my_board = Board.objects.get(id=board_id)
        board_pins = my_board.pins.values()
        html = "board_detail.html"
        context = {'board': my_board, 'board_pins': board_pins}
        return render(request, html, context)
