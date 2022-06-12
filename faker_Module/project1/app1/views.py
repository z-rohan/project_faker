from django.shortcuts import render,redirect
from .models import Student
from faker import Faker
import random

# Create your views here.
def ShowStudent(request):
    template_name='app1/showstudent.html'
    data=Student.objects.all()

    context={'obj':data}
    return render(request,template_name,context)

def FakeData(request):
    template_name='app1/showstudent.html'
    fake=Faker()
    for i in range(10):
        stu=Student()
        
        stu.sid=random.randint(0,999)
        stu.name=fake.name()
        stu.address=fake.address()
        stu.email=fake.email()
        
        stu.save()
    return redirect('showstudent_url')