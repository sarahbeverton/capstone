from boards.models import Board
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import View

from pinusers.models import PinUser

from .forms import UploadProfilePic

# Create your views here.


def profile(request, username):
    current_user = PinUser.objects.get(username=username)
    boards = Board.objects.filter(user=current_user)
    user_pins = current_user.pins.values().order_by('-created_at')
    following = list(current_user.following.values_list('username', flat=True))
    followers = PinUser.objects.filter(following=current_user)
    board_photos = {}

    for board in boards:
        board_photos[board.title] = board.pins.values_list('photo', flat=True)

    form = UploadProfilePic()

    context = {'boards': boards, 'pins': user_pins, 'pinuser': current_user,
               'following': following, 'followers': followers, 'board_photos': board_photos.items(),
               'form': form}

    if request.method == 'POST':
        form = UploadProfilePic(
            request.POST, request.FILES, instance=current_user)

        if form.is_valid():
            form.save()
            return render(request, 'profile.html', context)

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
