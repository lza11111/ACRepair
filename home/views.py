from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

# Create your views here.
class HomeViewSet(viewsets.GenericViewSet):

    @list_route(methods=['GET'], )
    def overview(self, request):
        return Response({
            'description': '这是公司简介'
        })