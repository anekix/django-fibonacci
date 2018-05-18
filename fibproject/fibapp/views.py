from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import View
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache

import json
import timeit

from .models import FibonacciNumber


def fib(n):
    'Find the n-th fibonacci number iteratively'
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# @method_decorator(cache_page(60 * 5), name='dispatch')
class FibonacciCalculatorView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'fib.html')
        pass

    def post(self, request):
        response = {'success': True, 'error': '',
                    'res': '', 'time': '', 'cached_result': False}
        nth_term = int(request.POST['nth_term'])

        # check if value is present in cache return it without computing or making a call to DB
        if nth_term in cache:
            start_time = timeit.default_timer()
            response['res'] = cache.get(nth_term)
            # print("GOT CACHED...............")
            elapsed = timeit.default_timer() - start_time
            response['time'] = elapsed
            response['cached_result'] = True
            return HttpResponse(
                json.dumps(response),
                content_type="application/json"
            )
        else:
            # if there was a cache miss, check if the value is present in DB, and
            # if present set the cache & return the result from DB, if value value is
            # not stored even in DB , then compute the result, set in DB, set Cache, return 

            start_time = timeit.default_timer()
            # check if the result is already present in db
            result = FibonacciNumber.objects.filter(nth_term=nth_term).first()

            if result:
                value = result.value
                response['res'] = value
                response['in_db'] = True
                print("already prsent in db...")
            else:
                value = fib(nth_term)
                FibonacciNumber.objects.create(
                    nth_term=nth_term,
                    value=value,
                )
                print("NOT PRESENT IN DB")
                response['res'] = value

            elapsed = timeit.default_timer() - start_time

            # set cache as there was a cache miss.
            cache.set(nth_term, value, timeout=900)

        response['time'] = elapsed

        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        )

