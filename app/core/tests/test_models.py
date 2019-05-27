from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ Test Creating a new User with email is successfull"""
        email = 'Test@gmail.com'
        password = 'test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password

        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        email = 'test@gmail.com'
        user = get_user_model().objects.create_user(email, 'test@123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test email with no error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@123')

    def test_create_new_superuser(self):
        """ Testing creating a new Superuser """
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
