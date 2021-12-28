from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
# from .cache import *
from .models import *
from django.conf import settings
from .ApiV1_0 import *


class UpsertLanguage(APIView):
    def post(self, request, format=None):

        request.data['PubIp'] = getUserIP(request)
        returnData = ApiLanguage.upsertLanguage(self, request.data)
        if returnData['RS'] == "SUCCESS":
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)