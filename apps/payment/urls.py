from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('complete/', views.payment_completed, name='complete'),
    path('canceled/', views.payment_canceled, name='cancel')
]
