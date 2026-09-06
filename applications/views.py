from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsRecruiter, IsCandidate
from .models import Application
from .serializers import ApplicationSerializer


class ApplicationCreateView(generics.CreateAPIView):

    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsCandidate]

    def perform_create(self, serializer):
        serializer.save(candidate=self.request.user)


class CandidateApplicationListView(generics.ListAPIView):

    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsCandidate]

    def get_queryset(self):

        queryset = Application.objects.filter(
            candidate=self.request.user
        ).order_by('-applied_at')

        status = self.request.query_params.get('status')

        if status:
            queryset = queryset.filter(status__iexact=status)

        return queryset


class RecruiterApplicationListView(generics.ListAPIView):

    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get_queryset(self):

        queryset = Application.objects.filter(
            job__recruiter=self.request.user
        ).order_by('-applied_at')

        status = self.request.query_params.get('status')

        if status:
            queryset = queryset.filter(status__iexact=status)

        return queryset


class ApplicationStatusUpadteView(generics.UpdateAPIView):

    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    http_method_names = ['patch']

    def get_queryset(self):
        return Application.objects.filter(
            job__recruiter=self.request.user
        )