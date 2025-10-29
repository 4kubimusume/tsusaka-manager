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
        self.assertEqual(Participant.objects.count(), 1)

    def test_create_view(self):
        response = self.client.post(reverse('participant_create'), {
            "name": "New User",
            "email": "new@example.com",
            "type": "ob",
        })
        self.assertEqual(response.status_code, 302)  # リダイレクト
        self.assertRedirects(response, reverse("participant_list"))
        self.assertTrue(Participant.objects.filter(name="New User").exists())

    def test_edit_view(self):
        response = self.client.post(reverse('participant_edit', args=[self.p1.id]), {
            "name": "Updated User",
            "email": "updated@example.com",
            "type": "student",
        })
        self.assertEqual(response.status_code, 302)  # リダイレクト
        self.p1.refresh_from_db()
        self.assertEqual(self.p1.name, "Updated User")
        self.assertEqual(self.p1.email, "updated@example.com")

    # def test_delete_view(self):
    #     response = self.client.post(reverse('participant_delete', args=[self.p1.id]))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertFalse(Participant.objects.filter(id=self.p1.id).exists())
