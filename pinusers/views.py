from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
#from django.utils import timezone

from pinusers.models import PinUser
from boards.models import Board
from pins.models import Pin
# Create your views here.


def profile(request, username):
    current_user = PinUser.objects.get(username=username)
    boards = Board.objects.filter(user=current_user)
    user_pins = current_user.pins.values().order_by('-created_at')
    following = list(current_user.following.values_list('username', flat=True))
    followers = PinUser.objects.filter(following=current_user)
    following_pins = Pin.objects.none()
    for user in following:
        following_user = PinUser.objects.get(username=user)
        following_user_pins = following_user.pins.values()
        following_pins = following_pins | following_user_pins
    all_following_pins = following_pins.distinct()
    following_photos = all_following_pins.values_list('photo', flat=True)
    board_photos = {}
    for board in boards:
        board_photos[board.title] = board.pins.values_list('photo', flat=True)
    context = {'boards': boards, 'pins': user_pins, 'pinuser': current_user,
               'following': following, 'followers': followers, 'board_photos': board_photos.items(),
               'following_pins': all_following_pins, 'following_photos': following_photos}
    return render(request, 'profile.html', context)


def following_pins(request, username):
    current_user = PinUser.objects.get(username=username)
    following = list(current_user.following.values_list('username', flat=True))
    following_pins = Pin.objects.none()
    for user in following:
        following_user = PinUser.objects.get(username=user)
        following_user_pins = following_user.pins.values()
        following_pins = following_pins | following_user_pins
    all_following_pins = following_pins.distinct()
    context = {'pins': all_following_pins}
    return render(request, 'following_pins.html', context)


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
