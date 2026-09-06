from django.urls import path
from .views import (ApplicationCreateView,
                    ApplicationStatusUpadteView,
                    RecruiterApplicationListView,
                    CandidateApplicationListView)

urlpatterns = [
    path('apply/', ApplicationCreateView.as_view(), name='apply-job'),
    path('my-applications/', CandidateApplicationListView.as_view(), name='my-applications'),
    path('recruiter/', RecruiterApplicationListView.as_view(), name='recruiter-applications'),
    path('<int:pk>/status/', ApplicationStatusUpadteView.as_view(), name='application-status'),

]