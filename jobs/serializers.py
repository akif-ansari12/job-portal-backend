from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):

    recruiter = serializers.ReadOnlyField(source='recruiter.username')

    class Meta:
        model = Job

        fields = [
            'id',
            'title',
            'company_name',
            'description',
            'location',
            'salary',
            'job_type',
            'recruiter',
            'created_at',
            'updated_at'
        ]

        read_only_fields = [
            'id',
            'recruiter',
            'created_at',
            'updated_at'
        ]
    