from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse
from .forms import ContactRequest


class TestContactForm(TestCase):

    def test_render_if_contact_page_has_contact_form(self):
        """Verifies if the contact page contains a contact web form"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context['contact_form'], ContactRequest)

    def test_successful_contact_form_submission(self):
        """Test for a user completed contact form"""

        self.user = User.objects.create_user(
            username="myUsername",
            password="myPassword",
            email="test@test.com")

        contact_data = {
            'name': 'test name',
            'topic': 'test topic',
            'email': 'test@email.com',
            'type_of_request': 'not specified',
            'message': 'test message'
        }

        response = self.client.post('/contact/', contact_data, follow=True)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your message has been received!')
