from projects.data import Data
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from projects.serializers import SumSerializer, ProjectParameterSerializer
from django.core.serializers.json import DjangoJSONEncoder
import json


class DataTest(APIView):
    def get(self, request):
        data = Data()
        return Response({'res': data.get_test_data()}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SumSerializer(data=request.data)
        if serializer.is_valid():
            n1 = serializer.validated_data['num1']
            n2 = serializer.validated_data['num2']
            data = Data()
            res = data.get_sum(n1, n2)
            return Response({'res': res}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectServices(APIView):
    def post(self, request):
        serializer = ProjectParameterSerializer(data=request.data)
        if serializer.is_valid():
            parameters = serializer.validated_data['parameters']
            data = Data()
            projects = data.get_projects(parameters)
            res = json.dumps(list(projects.values()), cls=DjangoJSONEncoder)
            return Response({'res': res}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
