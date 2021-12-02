import json

from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

from api.models import Realtors
from rest_framework import viewsets
from api.serializer import RealtorSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from django.http import HttpResponse
import datetime

# BUG

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Realtors, Realtors_detail, Realtors_list






@permission_classes((permissions.AllowAny,))

class Realtors_APIView(ListAPIView):
    queryset = Realtors.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = PageNumberPagination

    def get(self, request, format=None):

        # """
        # Return a list of all realtors.
        # """
        print("requeste_user", request.user)
        print("DATA",request.__dict__)
        print("PARAMS",request.query_params)
        print("ZIP CODE",request.query_params.get('zipcode'))
        page = self.paginate_queryset(self.queryset)
        print("PAGE",page)
        page_number = self.request.query_params.get('page_number ', 1)
        page_size = self.request.query_params.get('page_size ', 10)
        print("***",page,page_number,page_size)


        serializer = self.serializer_class(page, many=True)
        # serializer = RealtorSerializer(queryset, many=True)
        # response = Response(serializer.data, status=status.HTTP_200_OK)
        response = self.get_paginated_response(serializer.data)
        print("RESPONSE DATA",response.data)
        return Response({"realtors": response.data,"is_authenticated": "true" if request.user.is_authenticated else "false","params":request.query_params})
        # return Response

# used for SEAG
@permission_classes((permissions.AllowAny,))
class Realtors_APIView_2(APIView):

    def get(self, request, format=None):

        """" Return a list of all realtors"""

        zipcode = request.query_params.get('zipcode') # format: zipcodes coma separated: http://127.0.0.1:8000/api/realtor_2/?zipcode=28011,28240
        zipcode = zipcode.split(",") # convert to a list
        if zipcode is not None:
            # queryset = Realtors.objects.all().filter(zipcode= request.query_params['zipcode'])[:1000]
            # queryset = Realtors.objects.all().filter(zipcode__in = [28011,28240])[:1000]
            # queryset = Realtors.objects.all().filter(zipcode__in = zipcode)[:1000]
            queryset = Realtors_detail.objects.all().filter(zipcode__in = zipcode)[:1000]
        else:
            return Response("error: zipcode not in params", status.HTTP_400_BAD_REQUEST)

        serializer = RealtorSerializer(queryset,many=True)
        return Response(serializer.data)




class RealtorViewSet(APIView):

    """
    API endpoint that allows realtors to be viewed or edited.
    """

    queryset = Realtors.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = PageNumberPagination

    @permission_classes((permissions.AllowAny,))
    def get(self, request, *args, **kwargs):

        # """
        # Return a list of all realtors.
        # """
        print("requeste_user", request.user)
        print("DATA",request.__dict__)
        print("PARAMS",request.query_params)
        print("ZIP CODE",request.query_params.get('zipcode'))
        queryset = Realtors.objects.all()
        serializer = RealtorSerializer(queryset,many=True)
        # return Response({"user":json.dumps(request.user),"params":request.query_params,"results":serializer.data})
        return Response({"is_authenticated": "true" if request.user.is_authenticated else "false","params":request.query_params,"results":serializer.data})
    """   
    def get_queryset(self):
        # if self.request.method == 'GET': print('** GET METHOD')
        # zipcode = self.request.GET['zipcode']
        # zipcode = self.kwargs['zipcode']
        # print(zipcode)
        # print(self.kwargs)

        queryset = Realtors.objects.all()
        serializer = RealtorSerializer(queryset,many=True)
        # return Response(queryset.values())
        return Response(serializer.data)
        # return JsonResponse(serializer.data,safe=False)
        # return JsonResponse({"hello": 123})
    """
# FIXME TODO ALERT carlos
# TODO ñjdaskf lkadjsfka
# WATCH
# WARNING
# BUG
## BUG
# bug
# BUG kkuhadsfkjha lkj sad k




"""
API endpoint that allows realtors to be viewed or created.
"""

@api_view(['GET', 'POST'])
# @renderer_classes([JSONRenderer])
@permission_classes((permissions.AllowAny,))

def realtor_api_view(request):
    if request.method == 'GET':
        print("requeste_user",request.user)
        zipcode = request.data.get('zipcode')
        print("THIS IS THE ZIPCODE", zipcode)
        if zipcode is not None:
            realtors = Realtors.objects.all().filter(zipcode = request.data['zipcode'])
        else:
            realtors = Realtors.objects.all()
        serializer = RealtorSerializer(realtors,many=True)
        print(request.data)
        print(request.query_params)
        print(request.query_params.get('zipcode'))
        print(zipcode)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RealtorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)