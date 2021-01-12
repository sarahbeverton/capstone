from pinusers.models import PinUser

def following_context_processor(request):
    current_user = PinUser.objects.get(username=request.user.username)
    following = list(current_user.following.values_list('username', flat=True))
    data = {
        'following': following
    }

    return data