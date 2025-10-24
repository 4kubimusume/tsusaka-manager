from django.test import TestCase
from django.urls import reverse
from .models import Participant

class ParticipantModelTest(TestCase):
    def test_create_participant(self):
        p = Participant.objects.create(
            name="Test User",
            email="test@example.com",
            type="student"
        )
        self.assertEqual(p.name, "Test User")
        self.assertTrue(Participant.objects.exists())

class ParticipantViewTest(TestCase):
    def setUp(self):
        self.p1 = Participant.objects.create(
            name="User1",
            email="u1@example.com",
            type="student"
        )

    def test_list_view(self):
        response = self.client.get(reverse('participant_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User1")

    def test_create_view(self):
        response = self.client.post(reverse('participant_create'), {
            "name": "New User",
            "email": "new@example.com",
            "type": "ob",
        })
        self.assertEqual(response.status_code, 302)  # リダイレクト
        self.assertTrue(Participant.objects.filter(name="New User").exists())
