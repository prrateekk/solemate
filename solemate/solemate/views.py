from django.http import HttpResponse
from solemate.models import User
from rest_framework import viewsets
from rest_framework_mongoengine.serializers import DocumentSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the app index. What's going on?")


def profile(request):
    user = User.objects.all().first()
    return HttpResponse("Hello, {}. How's going on?".format(user.name))

class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = "__all__"

class SMModelViewSet(viewsets.ModelViewSet):
    def getValInFieldType(self, val, key, field):
        python_value = field.to_python(val)
        return python_value

    def updateQuerySet(self, qs, key, val):
        field = self.model._fields.get(key)
        if not field:
            return qs
        python_value = self.getValInFieldType(val, key, field)
        qs = qs.filter(**{key: python_value})
        return qs

    def get_queryset(self):
        assert self.queryset is None
        qs = self.model.objects
        print(self.request.query_params)
        for key, val in self.request.query_params.items():
            qs = self.updateQuerySet(qs, key, val)
        return qs

class UserViewSet(SMModelViewSet):
    model = User
    serializer_class = UserSerializer

