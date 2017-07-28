from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import *


from .models import *


class WMSUserViewSet(ViewSet):
    # base_url = r'/(?P<pk>\d+)/cpu'
    base_url = r'/users'
    base_name = ''

    @csrf_exempt
    def create(self, request):
        # if not request.user.is_authenticated():
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            data = request.data
            newuser = employe_details.objects.create(username=data['username'] if 'username' in data.keys() else "",
                                                     first_name=data[
                                                         'first_name'] if 'first_name' in data.keys() else "",
                                                     last_name=data['last_name'] if 'last_name' in data.keys() else "",
                                                     email=data['email'] if 'email' in data.keys() else "",
                                                     team=data['team'] if 'team' in data.keys() else "")
            password = data['password'] if 'password' in data.keys() else ""
            newuser.set_password(password)
            newuser.save()

            return Response({"result": "User created successfully", "status": True})

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):

        # if not request.user.is_authenticated():
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)

            if request.method == "GET":

                try:
                    page_limit = int(request.GET.get('page_limit', 10))  # Set the page limit
                    page = int(request.GET.get('page', 1))  # Set the current page
                except Exception as e:
                    page_limit = 10
                    page = 1

                page -= 1  # UI uses 1 based indexing, python 0
                export_ = request.GET.get('export', None)
                filter_ = request.GET.get('filter', None)
                sort_ = request.GET.get('sort', None)
                order_ = request.GET.get('order', None)

                users = employe_details.objects.all()



                message = {"result": users,
                           "number_of_rows": len(users),
                           "page": page + 1

                           }

                return Response(message)
    #
    # else:
    # return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # if not request.user.is_authenticated():
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)
        if employe_details.objects.filter(pk=pk).exists():
            return Response(employe_details.objects.get(pk=pk).json_ready())
        return Response(status=status.HTTP_401_UNAUTHORIZED)


