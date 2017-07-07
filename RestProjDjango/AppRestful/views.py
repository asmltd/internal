from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Userdetail, Student, Onsite, Session
from .serializers import UserdetailSerializer, StudentSerializer, OnsiteSerializer, SessionSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)


class UserdetailViewSet(viewsets.ModelViewSet):
    queryset = Userdetail.objects.all()
    serializer_class = UserdetailSerializer
    permission_classes = (IsAuthenticated,)
    # lookup_fields = ('Id')


class OnsiteViewSet(viewsets.ModelViewSet):
    queryset = Onsite.objects.all()
    serializer_class = OnsiteSerializer
    permission_classes = (IsAuthenticated,)


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        if not request.user.is_authenticated():
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if request.method == "GET":
            return Response({"username": request.user.username,"Email":request.user.email,"Id":request.user.id})

    def retrieve(self, request, code=None):
        if not request.user.is_authenticated():
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@login_required
def index(request):
    return render(request, 'index.html', {})


def signin(request):
    next = request.GET.get('next')
    if next is None and request.POST.get('next') is not None:
        next = request.POST.get('next')

    if next is None:
        next = "/"

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        # login(request, user)
        # return redirect("/")
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html', {'error': 'fail', 'next': next})

    else:
        return render(request, 'login.html', {'next': next})


@login_required
def signout(request):
    logout(request)
    return render(request, 'logout.html', {'error': ''})
