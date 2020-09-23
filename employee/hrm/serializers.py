from rest_framework import serializers
from hrm.models import Users

class UsersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    employee_id = serializers.CharField(required=False)
    experience = serializers.FloatField(required=False)

    class Meta:
        model = Users
        fields = '__all__'
        # fields = ('name', 'employee_id')