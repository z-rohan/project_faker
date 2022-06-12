from django.urls import path
from .views import *


urlpatterns=[
    path('ss/',ShowStudent,name='showstudent_url'),
    path('fd/',FakeData,name='fakedata_url'),
]