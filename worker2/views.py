from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from rest_framework.viewsets import ModelViewSet, ViewSet
from urllib.request import urlopen
# Create your views here.

from service import APIService

api = APIService()

class PostViewSet2(ViewSet):

       # api = APIService()
        # r = api.get('https://jsonplaceholder.typicode.com/posts/')
        # data = r.result().data
        # return Response(data)

    """
    A simple ViewSet for listing or retrieving post.
    """
    def list(self, request):

        api = APIService()
        r = api.get('https://jsonplaceholder.typicode.com/posts/')
        data = r.result().data
        return Response(data)
    
    def retrieve(self, request, id=None):
        data = json.load(urlopen('https://jsonplaceholder.typicode.com/posts/' + str(id)))
        return Response(data)