from django.urls import path
from base.views import contact

urlpatterns = [
    path('',contact),
]
