from django.shortcuts import render
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from pinusers.models import PinUser
from boards.models import Board

# Create your views here.

def profile(request):
    current_user = PinUser.objects.get(username=request.user.username)
    boards = Board.objects.filter(user=current_user)
    user_pins = current_user.pins.values()
    #following = list(current_user.following.values_list('username', flat=True))
    context = {'boards': boards, 'pins': user_pins, 'pinuser': current_user}
    return render(request, 'profile.html', context)

"""
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
"""