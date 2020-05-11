from django.shortcuts import render 
from django.http import HttpResponse 
from .form import RegNewUsr, RegNewTeacher, NewTest, Answer
from datetime import datetime
from .models import User, Test, Teacher, AnsRecived

# Create your views here.
def home(request):
    return render(request,'welcome.html')
def login(request):
    if request.method == 'POST':
        rollno = request.POST['rollno']
        username = request.POST['username']
        key = request.POST['password']
        if User.objects.filter(username__icontains=username):
            if User.objects.filter(rollno__icontains=rollno):
                if Test.objects.filter(key_or_passward_to_give_test_share__icontains=key):
                    test = Test.objects.filter(key_or_passward_to_give_test_share__icontains=key)
                    return render(request,'test.html',{'tes':test})
                else:
                    return render(request,'login.html',{'pas':'Incorrect Password(key). Ask Teacher correct key'})
            else:
                return render(request,'login.html',{'rol':'Incorrect Rollno'})
        else:
            return render(request,'login.html',{'usr':'Incorrect User Name'})
    else:
        return render(request,'login.html')
def teacher_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passward = request.POST['password']
        if Teacher.objects.filter(username__icontains=username):
            if Teacher.objects.filter(passward__icontains=passward):
                return render(request,'teacher.html',{'name':username})
            else:
                return render(request,'login_teacher.html',{'pas':'Incorrect Password'})
        else:
            return render(request,'login_teacher.html',{'usr':'Incorrect User Name'})
    else:
        return render(request,'login_teacher.html')

def test(request):
    if request.method == 'POST':
        form = Answer(request.POST)
        form.save()
        print('******************************************************************')
        return render(request,'welcome.html')

    else:
        return render(request,'login.html')
def register_teacher(request):
    form = RegNewTeacher()
    if request.method == 'POST':
        form = RegNewTeacher(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'wel.html')
        else:
            return render(request,'register_teacher.html',{'form':form})

    else :
        return render(request,'register_teacher.html',{'form':form})

def register_student(request):
    form = RegNewUsr()
    if request.method == 'POST':
        form = RegNewUsr(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'wel.html')
        else:
            return render(request,'register.html',{'form':form})

    else :
        return render(request,'register.html',{'form':form})

def creat_test(request):
    form = NewTest()
    if request.method == 'POST':
        form = NewTest(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'wel.html')
        else:
            return render(request,'newtest.html',{'form':form})

    else :
        return render(request,'newtest.html',{'form':form})

def check(request):
    if request.method == 'POST':
        key = request.POST['key']
        if key:
            match = AnsRecived.objects.filter(key__icontains=key)
            print('key is ' , key)
            if match :
                print(match)
                return render(request,'check.html',{'res':match})
        else:
            return render(request,'check.html')

    else :
        return render(request,'check.html')
