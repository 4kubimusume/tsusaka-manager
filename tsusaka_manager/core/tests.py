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

    def test_delete_view(self):
        p = Participant.objects.create(
            name="Delete Me",
            email="delete@example.com",
            type="student",
        )
        response = self.client.post(reverse('participant_delete', args=[p.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('participant_list'))
        self.assertFalse(Participant.objects.filter(id=p.id).exists())

class ParticipantInvalidInputTest(TestCase):

    def test_create_with_empty_name(self):
        response = self.client.post(reverse('participant_create'), {
            "name": "",
            "email": "valid@example.com",
            "type": "student",
        })
        # print(response.status_code)
        # print(response.context)
        self.assertEqual(response.status_code, 200)
        # self.assertFormError(response, 'form', 'name', 'このフィールドは必須です。')
        self.assertFormError(response.context['form'], 'name', 'This field is required.')
        self.assertEqual(Participant.objects.count(), 0)

    def test_create_with_invalid_email(self):
        response = self.client.post(reverse('participant_create'), {
            "name": "Bad Email",
            "email": "notanemail",
            "type": "student",
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email', '有効なメールアドレスを入力してください。')
        self.assertEqual(Participant.objects.count(), 0)

    def test_edit_nonexistent_participant(self):
        """存在しないIDで編集しようとしたら404"""
        response = self.client.get(reverse('participant_edit', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_delete_with_get_does_not_delete(self):
        """GETアクセスでは削除しない"""
        p = Participant.objects.create(
            name="Safe User",
            email="safe@example.com",
            type="student"
        )
        response = self.client.get(reverse('participant_delete', args=[p.id]))
        self.assertEqual(response.status_code, 200)
        # GETでは削除されていない
        self.assertTrue(Participant.objects.filter(id=p.id).exists())

    def test_delete_nonexistent_participant(self):
        """存在しないIDを削除しようとしたら404"""
        response = self.client.post(reverse('participant_delete', args=[999]))
        self.assertEqual(response.status_code, 404)
