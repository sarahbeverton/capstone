from boards.models import Board
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect, redirect, render, reverse
from django.views.generic import View
from pinusers.models import PinUser

from pins.forms import PinForm
from pins.models import Comment, Pin

from .forms import CommentForm

# Create your views here.


class PinView(LoginRequiredMixin, View):
    def get(self, request, pin_id):
        my_pin = Pin.objects.get(id=pin_id)
        comments = Comment.objects.filter(pin=my_pin)
        current_user = PinUser.objects.get(username=request.user.username)
        user_boards = Board.objects.filter(user=current_user)
        user_pins = list(current_user.pins.values_list('title', flat=True))
        html = "pin_detail.html"
        form = CommentForm()
        context = {'pin': my_pin, 'boards': user_boards,
                   'user_pins': user_pins, 'comment_form': form,
                   'comments': comments}
        return render(request, html, context)

    def post(self, request, pin_id):
        if request.method == 'POST':
            my_pin = Pin.objects.get(id=pin_id)
            current_user = PinUser.objects.get(username=request.user.username)
            user_boards = Board.objects.filter(user=current_user)
            comments = Comment.objects.filter(pin=my_pin)
            user_pins = list(current_user.pins.values_list('title', flat=True))
            form = CommentForm(request.POST or None)
            html = "pin_detail.html"
            if form.is_valid():
                content = request.POST.get('content')
                comment = Comment.objects.create(
                    pin=my_pin, author=request.user, content=content)
                comment.save()
                context = {'pin': my_pin, 'boards': user_boards,
                           'user_pins': user_pins, 'comment_form': form,
                           'comments': comments}
                return render(request, html, context)


class SaveView(LoginRequiredMixin, View):
    def get(self, request, pin_id):
        my_pin = Pin.objects.get(id=pin_id)
        request.user.pins.add(my_pin)
        return redirect("profile", username=request.user.username)


class RemovePinView(LoginRequiredMixin, View):
    def get(self, request, pin_id):
        current_user = PinUser.objects.get(username=request.user.username)
        user_boards = Board.objects.filter(user=current_user)
        my_pin = Pin.objects.get(id=pin_id)
        for board in user_boards:
            board_pin_titles = list(board.pins.values_list('title', flat=True))
            if my_pin.title in board_pin_titles:
                board.pins.remove(my_pin)
        current_user.pins.remove(my_pin)
        return redirect("profile", username=current_user.username)


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
            current_user = PinUser.objects.get(username=request.user.username)
            my_pin = Pin.objects.create(
                title=data['title'],
                author=current_user,
                description=data['description'],
                photo=data['photo'],
                url=data['url'],
            )
            my_pin.save()
            request.user.pins.add(my_pin)
            return redirect("profile", username=request.user.username)


def like_view(request, pin_id):
    pin = Pin.objects.filter(id=pin_id).first()
    pin.likes += 1
    pin.save()
    return HttpResponseRedirect(reverse("pin_detail", kwargs={'pin_id': pin_id}))
