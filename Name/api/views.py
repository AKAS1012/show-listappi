from rest_framework.decorators import api_view
from .models import Student
from .serializers import Studentserializers
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def show_list(request):
    if request.method == "GET":
        data = Student.objects.all()
        serializers = Studentserializers(data, many=True)
        return Response(serializers.data)
    elif request.method == "POST":
        serializers = Studentserializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
