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
                                    data={'nth_term': 5},
                                    )
        request.user = self.user

        response = FibonacciCalculatorView.as_view()(request)
        print (response.content)
        self.assertEqual(response.status_code, 200)


class UserLoginTest(TestCase):
        def test_fib_calculator_connect_to_correct_view(self):
            resolver = resolve('/accounts/login/')
            self.assertEqual(resolver.view_name, 'login')

        # test for logging-in is not Required , its a built-in view







        # resolver = resolve('/calculator/fib/')
        # self.assertEqual(resolver.view_name, 'fib_calculate')

    # def test_root_url_resolves_to_home_page_view(self):
    #     resolver = resolve('/calculator/fib/')
    #     self.assertEqual(resolver.view_name, 'fib_calculate')


# class DBLevelCacheTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         #Create 13 authors for pagination tests
#         # number_of_authors = 13
#         # for author_num in range(number_of_authors):
#         #     Author.objects.create(first_name='Christian %s' % author_num, last_name = 'Surname %s' % author_num,)

#         # create a enrty in DB
#         FibonacciNumber.objects.create(nth_term=5, value='120')


#     def test_is_db_level_cache_active(self):
#         resp =

#     def test_view_url_exists_at_desired_location(self):
#         resp = self.client.get('/catalog/authors/')
#         self.assertEqual(resp.status_code, 200)

#     def test_view_url_accessible_by_name(self):
#         resp = self.client.get(reverse('authors'))
#         self.assertEqual(resp.status_code, 200)

#     def test_view_uses_correct_template(self):
#         resp = self.client.get(reverse('authors'))
#         self.assertEqual(resp.status_code, 200)

#         self.assertTemplateUsed(resp, 'catalog/author_list.html')

#     def test_pagination_is_ten(self):
#         resp = self.client.get(reverse('authors'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertTrue('is_paginated' in resp.context)
#         self.assertTrue(resp.context['is_paginated'] == True)
#         self.assertTrue( len(resp.context['author_list']) == 10)

#     def test_lists_all_authors(self):
#         #Get second page and confirm it has (exactly) remaining 3 items
#         resp = self.client.get(reverse('authors')+'?page=2')
#         self.assertEqual(resp.status_code, 200)
#         self.assertTrue('is_paginated' in resp.context)
#         self.assertTrue(resp.context['is_paginated'] == True)
#         self.assertTrue( len(resp.context['author_list']) == 3)
