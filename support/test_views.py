from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import RespondForm, SupportForm
from .models import Support


class TestSupportPostViews(TestCase):
    """Pre-setup a superuser for tests & Give detail to a support post"""
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.support = Support(
            topic="support topic",
            parent=self.user,
            slug="support-topic",
            content="support content",
            status=1
        )
        self.support.save()

    def test_render_support_detail_page_with_comment_form(self):
        """Is the posting of a support request functional?"""
        response = self.client.get(reverse(
            'support_detail', args=['support-topic']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"support topic", response.content)
        self.assertIn(b"support content", response.content)
        self.assertIsInstance(
            response.context['reply_form'], RespondForm)

    def test_successful_reply_submission(self):
        """Test for adding a reply to a Support post"""
        self.client.login(
            username="myUsername", password="myPassword")
        reply_data = {
            'body': 'This is a test reply.'
        }
        response = self.client.post(reverse(
            'support_detail', args=['support-topic']), reply_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'This reply is awaiting approval',
            response.content
        )


class TestSupportPost(TestCase):
    """Creates test user & support post content"""
    def setUp(self):
        self.user = User.objects.create_user(
            username="myUsername",
            password="myPassword",
            email="test@test.com")

        self.support_post = Support(
            topic="The question that I have",
            content="hesitate",
            parent=self.user)
        self.support_post.save()

    def test_render_support_post_page_with_user_form(self):
        """Verifies get request for support post page
        containing a support post user form"""
        response = self.client.get('/support_post/')
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'Add your', response.content)
        self.assertIsInstance(
            response.context['support_form'], SupportForm)
