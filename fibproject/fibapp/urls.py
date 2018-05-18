# pages/urls.py
from django.urls import path

from . import views
from .views import FibonacciCalculatorView

urlpatterns = [
    # path('', views.homePageView, name='home'),
    # path('login/', views.Login, name='login'),
    path('fib/', FibonacciCalculatorView.as_view(), name='fib_calculate'),
    # path('login/', LoginView.as_view()),

]
