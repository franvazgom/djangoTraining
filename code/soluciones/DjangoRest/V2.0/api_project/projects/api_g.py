from projects.data import Data
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SumSerializer, ProjectParameterSerializer
import json
from django.core.serializers.json import DjangoJSONEncoder

class DataTest(APIView):
    def get(self, request):
        data = Data()
        return Response({'res':data.get_test_data()}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SumSerializer(data = request.data)
        if serializer.is_valid():
            num1 = serializer.validated_data['num1']
            num2 = serializer.validated_data['num2']
            data = Data()
            return Response({'res':data.get_sum(num1, num2)}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectServices(APIView):
    def post(self, request):
        serializer = ProjectParameterSerializer(data = request.data)
        if serializer.is_valid():
            parameters = serializer.validated_data['parameters']
            data = Data()
            projects = data.get_projects(parameters)
            res = json.dumps(list(projects.values()), cls=DjangoJSONEncoder)
            return Response({'res':res}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

