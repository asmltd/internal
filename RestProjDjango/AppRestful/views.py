from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Userdetail, Student
from .serializers import UserdetailSerializer, StudentSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

class UserdetailViewSet(viewsets.ModelViewSet):
    queryset = Userdetail.objects.all()
    serializer_class = UserdetailSerializer
    permission_classes = (IsAuthenticated,)
    #lookup_fields = ('Id')
    
@login_required
def index(request):
    return render(request, 'home.html', {})

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
        #login(request, user)
	#return redirect("/")
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



