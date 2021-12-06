from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, views
from logisticapp.models import RequestHeader
from logisticapp.serializers import LogisticExpensesSerializer
# Create your views here.


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