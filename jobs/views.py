from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Job
from .serializers import JobSerializer
from accounts.permissions import IsRecruiter
from .permissions import IsRecruiterOwner


class JobListCreateView(generics.ListCreateAPIView):

    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = Job.objects.all().order_by('-created_at')

        search = self.request.query_params.get('search')
        location = self.request.query_params.get('location')
        job_type = self.request.query_params.get('job_type')

        if search:
            queryset = queryset.filter(
                title__icontains=search
            ) | queryset.filter(
                company_name__icontains=search
            ) | queryset.filter(
                description__icontains=search
            )

        if location:
            queryset = queryset.filter(
                location__icontains=location
            )

        if job_type:
            queryset = queryset.filter(
                job_type__iexact=job_type
            )

        return queryset

    def get_permissions(self):

        if self.request.method == 'POST':
            return [IsAuthenticated(), IsRecruiter()]

        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):

        if self.request.method == 'GET':
            return [IsAuthenticated()]

        return [
            IsAuthenticated(),
            IsRecruiterOwner()
        ]