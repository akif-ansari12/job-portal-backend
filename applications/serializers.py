from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):

    candidate = serializers.ReadOnlyField(source='candidate.username')
    job_title = serializers.ReadOnlyField(source='job.title')

    class Meta:
        model = Application

        fields = [
            'id',
            'candidate',
            'job',
            'job_title',
            'resume',
            'cover_letter',
            'status',
            'applied_at',
            'updated_at'
        ]

        read_only_fields = [
                    'id',
                    'candidate',
                    'job_title',
                    'applied_at',
                    'updated_at'
]
        

    def validate(self, data):

        request = self.context.get('request')
        job = data.get('job')

        if request and request.user.is_authenticated:
            if Application.objects.filter(
                candidate=request.user,
                job=job
            ).exists():
                raise serializers.ValidationError(
                    "You have already applied for this job."
                )

        return data