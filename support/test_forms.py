from django.test import TestCase
from .forms import RespondForm


class TestRespondForm(TestCase):

    def test_form_is_valid(self):
        respond_form = RespondForm({'body': 'This is a great post'})
        self.assertTrue(respond_form.is_valid(), msg='Form is not valid')
