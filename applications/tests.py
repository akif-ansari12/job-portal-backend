from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from accounts.models import Profile
from jobs.models import Job


class ApplicationAPITest(APITestCase):

    def setUp(self):

        self.candidate = User.objects.create_user(
            username='testcandidate',
            password='Test@123'
        )

        Profile.objects.create(
            user=self.candidate,
            role='candidate'
        )

        self.recruiter = User.objects.create_user(
            username='testrecruiter',
            password='Test@123'
        )

        Profile.objects.create(
            user=self.recruiter,
            role='recruiter'
        )

        self.job = Job.objects.create(
            title='Python Developer',
            company_name='Test Company',
            description='Python backend job',
            location='Noida',
            salary=500000,
            job_type='Full Time',
            recruiter=self.recruiter
        )

    def test_candidate_can_apply(self):

        self.client.force_authenticate(
            user=self.candidate
        )

        response = self.client.post(
            '/api/applications/apply/',
            {
                'job': self.job.id,
                'cover_letter': 'I am interested in this job.'
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_candidate_cannot_apply_twice(self):

        self.client.force_authenticate(
            user=self.candidate
        )

        data = {
            'job': self.job.id,
            'cover_letter': 'First application'
        }

        first_response = self.client.post(
            '/api/applications/apply/',
            data
        )

        self.assertEqual(
            first_response.status_code,
            status.HTTP_201_CREATED
        )

        second_response = self.client.post(
            '/api/applications/apply/',
            data
        )

        self.assertEqual(
            second_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_recruiter_cannot_apply(self):

        self.client.force_authenticate(
            user=self.recruiter
        )

        response = self.client.post(
            '/api/applications/apply/',
            {
                'job': self.job.id,
                'cover_letter': 'Recruiter trying to apply.'
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_candidate_cannot_update_application_status(self):

        self.client.force_authenticate(
            user=self.candidate
        )

        response = self.client.post(
            '/api/applications/apply/',
            {
                'job': self.job.id,
                'cover_letter': 'My application'
            }
        )

        application_id = response.data['id']

        response = self.client.patch(
            f'/api/applications/{application_id}/status/',
            {
                'status': 'Shortlisted'
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_recruiter_can_update_own_application_status(self):

        self.client.force_authenticate(
            user=self.candidate
        )

        response = self.client.post(
            '/api/applications/apply/',
            {
                'job': self.job.id,
                'cover_letter': 'My application'
            }
        )

        application_id = response.data['id']

        self.client.force_authenticate(
            user=self.recruiter
        )

        response = self.client.patch(
            f'/api/applications/{application_id}/status/',
            {
                'status': 'Shortlisted'
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['status'],
            'Shortlisted'
        )