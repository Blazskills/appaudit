from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, views
from logisticapp.models import AuditLog, RequestHeader
from logisticapp.serializers import AuditDataLog, LogisticExpensesSerializer
# Create your views here.
from django.urls import resolve
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
# import pandas as pd
from array import *


class AuditData(APIView):
    def get(self, request):
        auditlog = AuditLog.objects.all()
        audited_serializer = AuditDataLog(auditlog, many=True)
        return Response(audited_serializer.data, status=status.HTTP_200_OK)
    # return Response('error':error)


class LogisticExpenseHeaderCreate(APIView):
    serializer_class = LogisticExpensesSerializer

    def post(self, request):
        logexpdata = request.data
        serializer = self.serializer_class(data=logexpdata)
        serializer.is_valid(raise_exception=True)
        requestheader_name_data = serializer.validated_data.get(
            'requestheader_name')
        department_header_onwer_data = serializer.validated_data.get(
            'department_header_onwer')
        if not RequestHeader.objects.filter(requestheader_name=requestheader_name_data, department_header_onwer=department_header_onwer_data).first():
            serializer.save()
            user_data = serializer.data
            response_dict = {"status": status.HTTP_201_CREATED,
                             "msg": 'created', 'data': user_data}
            return Response(response_dict,  status=status.HTTP_201_CREATED)
            # return Response({"message": "Request Header Title created successfully"} ,user_data, status=status.HTTP_201_CREATED)
        return Response({"error": "Request header name belongs to the same department, kindly choose a new department or new expenses header or title"}, status=status.HTTP_400_BAD_REQUEST)


'''
class TestRequestHeader(APIView):
    def get(self, request):
        current_site = get_current_site(request).domain
        try:
            browser_gangan = request.META['HTTP_SEC_CH_UA']
            HTTP_forward=request.META['HTTP_X_FORWARDED_FOR']

        except:
            browser_gangan = None
            HTTP_forward=None

        # user=''
        # if request.user:
        #         user=request.user
        #         print(user.id)
        # elif request.user.is_Anonymous():
        #         user = 'None'
        #         print(user)
        from django.forms.models import model_to_dict
      

        if not request.method in ('HEAD', 'OPTIONS', 'TRACE'):
            if hasattr(request, 'user') and request.user.is_authenticated:
                user = request.user
                userz = {
                    'userid': user.id
                }

                # print(model_to_dict(user))
            elif request.user.is_anonymous:
                userz = {
                    'userid':None
                }
                user = None
                print( 'user not log')
               

        resp_dict={
            'user': userz,
            'browser_gangan':browser_gangan,
            'HTTP_X_FORWARDED_FOR': HTTP_forward,
            'REMOTE_ADDR': request.META['REMOTE_ADDR'],
            'REQUEST_METHOD': request.META['REQUEST_METHOD'],
            'SERVER_NAME': request.META['SERVER_NAME'],
            'SERVER_PORT': request.META['SERVER_PORT'],
            'SERVER_PROTOCOL': request.META['SERVER_PROTOCOL'],
            'REQUEST_METHOD': request.META['REQUEST_METHOD'],
            'PATH_INFO': request.META['PATH_INFO'],
            'QUERY_STRING': request.META['QUERY_STRING'],       
            'user_currrent_browser': request.META['HTTP_USER_AGENT'],
            'CONTENT_TYPE': request.META['CONTENT_TYPE'],
            'path': request.path,
            'User-Agent': request.headers['User-Agent'],
            'currentsite':current_site
        }
        from django.http import HttpResponse

        print(HttpResponse.status_code)
        return Response(resp_dict,  status=status.HTTP_201_CREATED)
        
'''


class RequestLogs(APIView):
    def get(self, request, extra_context=None):
        auditlog = AuditLog.objects.all()
        audit_statchat = {
            'windows': AuditLog.objects.filter(operating_system='Windows').count(),
            'iphone': AuditLog.objects.filter(operating_system='Iphone').count(),
            'android': AuditLog.objects.filter(operating_system='Android').count(),
            'ipad': AuditLog.objects.filter(operating_system='Ipad').count(),
            'postman': AuditLog.objects.filter(operating_system='Postman').count(),
            'others': AuditLog.objects.filter(operating_system='Others').count()
        }
        operating_system_list = [audit_statchat['windows'], audit_statchat['iphone'], audit_statchat['android'],
                                 audit_statchat['ipad'], audit_statchat['postman'], audit_statchat['others']]
        context = {
            "auditlog": auditlog,
            "operating_system_list": operating_system_list
        }
        return render(request, "audit/requestlog.html", context)
