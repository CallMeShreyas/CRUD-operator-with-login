from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from superuser.models import Employee
# Create your views here.


def login(request):
    return render(request, 'userlogin.html')


def signup(request):
    return render(request, 'signup.html')


def signup_index(request):
    uname = request.POST.get('uname', 'default')
    upassword = request.POST.get('upassword', 'default')
    upasswordagain = request.POST.get('upasswordagain', 'default')
    count = 0
    user = User.objects.all()
    for item in user:
        if(item.username == uname):
            count = count+1

    if(count != 0 or upassword != upasswordagain):
        return HttpResponse('<h1>Sign Up Failed</h1><br><a href="/user/signup">Try Again </a>')
    else:
        user_obj = User(username=uname, password=upassword)
        user_obj.save()
        return HttpResponse('<h1> SignUp Successfull !!</h1><br><a href="/user/login"> Back To Login </a>')


def login_index(request):
    uname = request.POST.get('uname', 'default')
    upassword = request.POST.get('upassword', 'default')
    user = User.objects.get(username=uname)

    if(user.password == upassword):
        employee = Employee.objects.all()
        return render(request, 'show_user.html', {'employee': employee})
    else:
        return HttpResponse('<h1>Invalid Credentials</h1><br><a href="/user/login"> Retry To Login</a>')


def work_add(request):
    return render(request, 'add_user.html')


def work_add_status(request):
    iid = request.POST.get('eid', 'default')
    iname = request.POST.get('ename', 'default')
    iemail = request.POST.get('eemail', 'default')
    icontact = request.POST.get('econtact', 'default')
    employee = Employee(eid=iid, ename=iname, eemail=iemail, econtact=icontact)

    employee.save()

    return HttpResponse('<h1> Saved Successfully !!!<br><a href="/user/login_index/updated">Back To Main Page </a></h1>')


def updated(request):
    employee = Employee.objects.all()
    return render(request, 'show_user.html', {'employee': employee})
