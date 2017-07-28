import logging

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

logger = logging.getLogger(__name__)


class BaseViewSet(ViewSet):
    base_url = '/'
    base_name = 'viewset'

    def list(self, request):
        return Response()

    def create(self, request):
        return Response()

    def retrieve(self, request, pk=None):
        return Response()

    def update(self, request, pk=None):
        return Response()

    def partial_update(self, request, pk=None):
        return Response()

    def destroy(self, request, pk=None):
        return Response()


class BaseModelViewSet(ModelViewSet, BaseViewSet):
    base_url = '/'
    base_name = 'modelviewset'