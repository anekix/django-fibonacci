from django.test import TestCase
from django.test import TestCase, RequestFactory
from fibapp.models import FibonacciNumber
from django.contrib.auth.models import User
from django.urls import resolve
from django.views.generic.edit import View

import json

from .views import FibonacciCalculatorView


class URLResolversTest(TestCase):

    def test_fib_calculator_connect_to_correct_view(self):
        resolver = resolve('/calculator/fib/')
        self.assertEqual(resolver.view_name, 'fib_calculate')


class FibonacciCalculatorTest(TestCase):
    def setUp(self):
        self.post_data = {'nth_term': 5}
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='sadnhgftr65')

    def test_url_connect_to_correct_view(self):
        request = self.factory.post('/calculator/fib/',
                                    data={'nth_term': 9},
                                    )
        request.user = self.user

        response = FibonacciCalculatorView.as_view()(request)
        decoded_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(decoded_response['res'], 34)
        self.assertEqual(response.status_code, 200)


class UserLoginTest(TestCase):
        def test_fib_calculator_connect_to_correct_view(self):
            resolver = resolve('/accounts/login/')
            self.assertEqual(resolver.view_name, 'login')

