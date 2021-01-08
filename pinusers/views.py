from django.shortcuts import render

from pinusers.models import PinUser
from boards.models import Board

# Create your views here.


def profile(request):
    current_user = PinUser.objects.get(username=request.user.username)
    boards = Board.objects.filter(user=current_user)
    user_pins = current_user.pins.values()
    context = {'boards': boards, 'pins': user_pins}
    return render(request, 'profile.html', context)
