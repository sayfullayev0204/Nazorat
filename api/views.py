from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from django.contrib.auth.hashers import make_password
from .models import Teachers,Group,Appartment,Stiuation,Students
from .serializers import TeachersSerializer
from rest_framework.permissions import IsAuthenticated

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user  
        serializer = TeachersSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Teachers, Group, Students, Appartment, Stiuation
from .serializers import TeacherSerializer, GroupSerializer, StudentSerializer, AppartmentSerializer, StiuationSerializer


class HomeAPIView(APIView):
    def get(self, request):
        teacher = Teachers.objects.get(username=request.user.username)
        data = TeacherSerializer(teacher).data
        return Response(data)


class GroupDetailAPIView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentsInGroupAPIView(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return Students.objects.filter(group_id=group_id)


class ApartmentDetailAPIView(RetrieveAPIView):
    queryset = Appartment.objects.all()
    serializer_class = AppartmentSerializer


class ApartmentStudentsAPIView(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        appartment_id = self.kwargs['appartment_id']
        return Students.objects.filter(appartment_id=appartment_id)


class ApartmentSituationAPIView(APIView):
    def get(self, request, pk):
        try:
            appartment = Appartment.objects.get(pk=pk)
            situations = Stiuation.objects.filter(appartment=appartment)
            serializer = StiuationSerializer(situations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Appartment.DoesNotExist:
            return Response(
                {"error": "Appartment not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

    def post(self, request, pk):
        try:
            appartment = Appartment.objects.get(pk=pk)
            data = request.data.copy()
            data['appartment'] = appartment.id
            serializer = StiuationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Appartment.DoesNotExist:
            return Response(
                {"error": "Appartment not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
