from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from pinusers.models import PinUser
from boards.models import Board

# Create your views here.


def profile(request, username):
    current_user = PinUser.objects.get(username=username)
    boards = Board.objects.filter(user=current_user)
    user_pins = current_user.pins.values().order_by('-created_at')
    following = list(current_user.following.values_list('username', flat=True))
    followers = PinUser.objects.filter(following=current_user)
    board_photos = {}
    grab_first_photo = []

    for board in boards:
        board_photos[board.title] = board.pins.values_list('photo', flat=True)
    context = {'boards': boards, 'pins': user_pins, 'pinuser': current_user,
               'following': following, 'followers': followers, 'board_photos': board_photos.items()}
        
    return render(request, 'profile.html', context)


class FollowView(LoginRequiredMixin, View):
    def get(self, request, username):
        my_user = PinUser.objects.get(username=username)
        request.user.following.add(my_user)
        return redirect("profile", username=username)


class UnfollowView(LoginRequiredMixin, View):
    def get(self, request, username):
        my_user = PinUser.objects.get(username=username)
        request.user.following.remove(my_user)
        return redirect("profile", username=username)
