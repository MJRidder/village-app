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

    # def test_successful_contact_form_submission(self):
    #     """Test for a user completed contact form"""
    #     post_data = {
    #         'name': 'test name',
    #         'topic': 'test topic',
    #         'email': 'test@email.com',
    #         'type of request': 'not specified',
    #         'message': 'test message'
    #     }
    #     response = self.client.post('contact/contact.html', post_data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(
    #         b'Your message has been received! We hope to get 
    #           back to you as soon as possible!', response.content
    #         )
