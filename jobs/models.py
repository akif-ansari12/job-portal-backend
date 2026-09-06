from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):

    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),

    ]

    title       = models.CharField(max_length=200)
    company_name     = models.CharField(max_length=200)
    description = models.TextField()
    location    = models.CharField(max_length=100)
    salary      = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    job_type    = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    recruiter   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    created_at   = models.DateTimeField(auto_now=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

