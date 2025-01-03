from rest_framework import serializers
from .models import Teachers


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ["id", "username", "first_name", "last_name"]

from rest_framework import serializers
from .models import Teachers, Group, Students, Appartment, Stiuation

class TeacherSerializer(serializers.ModelSerializer):
    student_count = serializers.IntegerField(source='students_set.count', read_only=True)
    group_count = serializers.IntegerField(source='group_set.count', read_only=True)
    male_students_count = serializers.SerializerMethodField()
    female_students_count = serializers.SerializerMethodField()

    class Meta:
        model = Teachers
        fields = ['id', 'username', 'first_name', 'last_name', 'student_count', 'group_count', 'male_students_count', 'female_students_count']

    def get_male_students_count(self, obj):
        return Students.objects.filter(tutor=obj, type="ERKAK").count()

    def get_female_students_count(self, obj):
        return Students.objects.filter(tutor=obj, type="AYOL").count()


class GroupSerializer(serializers.ModelSerializer):
    student_count = serializers.IntegerField(source='students_set.count', read_only=True)
    appartment_count = serializers.IntegerField(source='appartment_set.count', read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'student_count', 'appartment_count']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'firstname', 'lastname', 'type']

class AppartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appartment
        fields = ['id', 'appartment_user_firstname', 'appartment_user_lastname', 'info']



class StiuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stiuation
        fields = [
            'id',
            'appartment',
            'room_situation',
            'heating_system',
            'kitchen_system',
            'description',
            'imge_1',
            'imge_2',
            'imge_3',
        ]
