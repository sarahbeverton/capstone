from django.shortcuts import render

from pinusers.models import PinUser
from boards.models import Board

# Create your views here.


def profile(request):
    current_user = PinUser.objects.get(username=request.user.username)
    boards = Board.objects.filter(user=current_user)
    context = {'boards': boards}
    return render(request, 'profile.html', context)
