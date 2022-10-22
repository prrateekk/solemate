from django.http import HttpResponse
from solemate.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the app index. What's going on?")


def profile(request):
    user = User.objects.all().first()
    return HttpResponse("Hello, {}. How's going on?".format(user.name))
