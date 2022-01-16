from django.shortcuts import render
from django.http import HttpResponse
from .models import Superuser, Employee
# Create your views here.


def superlogin(request):
    return render(request, 'superlogin.html')


def superlogin_index(request):
    employee = Employee.objects.all()
    sname = request.POST.get('sname', 'default')
    spassword = request.POST.get('spassword', 'default')

    super_obj = Superuser.objects.get(supername=sname)

    if(super_obj.password == spassword):
        # return HttpResponse('<h1>User Login Success !!!</h1>')
        return render(request, 'show_superuser.html', {'employee': employee})
    else:
        return HttpResponse('<h1>Superuser Login FAILED !!!</h1><a href="/superuser"><button>Retry Again </button></a>')


def work_add(request):
    return render(request, 'add.html')


def work_add_status(request):
    iid = request.POST.get('eid', 'default')
    iname = request.POST.get('ename', 'default')
    iemail = request.POST.get('eemail', 'default')
    icontact = request.POST.get('econtact', 'default')
    employee = Employee(eid=iid, ename=iname, eemail=iemail, econtact=icontact)

    employee.save()

    return HttpResponse('<h1> Saved Successfully !!!<br><a href="/superuser/superlogin_index/updated"><button>Back To Main Page </button></a></h1>')


def work_edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def work_update(request, id):
    employee = Employee.objects.get(id=id)
    iid = request.POST.get('eid', 'default')
    iname = request.POST.get('ename', 'default')
    iemail = request.POST.get('eemail', 'default')
    icontact = request.POST.get('econtact', 'default')

    employee.eid = iid
    employee.ename = iname
    employee.eemail = iemail
    employee.econtact = icontact

    employee.save()

    return HttpResponse('<h1> Updated Successfully !!!<br><a href="/superuser/superlogin_index/updated"><button>Back To Main Page </button></a></h1>')


def work_delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return HttpResponse('<h1> Record Deleted Successfully !!!<br><a href="/superuser/superlogin_index/updated"><button>Back To Main Page </button></a></h1>')


def updated(request):
    employee = Employee.objects.all()
    return render(request, 'show_superuser.html', {'employee': employee})


def work_addpoint(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'addpoint.html', {'employee': employee})


def work_addpoint_status(request, id):
    addpt = request.POST.get('addpt', 'default')
    # print(addpt)
    addpt = int(addpt)
    employee = Employee.objects.get(id=id)
    v1 = employee.epoints
    v1 = int(v1)
    # print(v1)
    v1 = v1 + addpt
    employee.epoints = v1
    employee.save()

    return HttpResponse('<h1> Added Successfully !!!<br><br><a href="/superuser/superlogin_index/updated"><button>Back To Main Page </button></a></h1>')


def work_withdraw(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'withdraw.html', {'employee': employee})


def work_withdraw_status(request, id):
    withdr = request.POST.get('withdr', 'default')
    withdr = int(withdr)
    employee = Employee.objects.get(id=id)
    v2 = employee.epoints
    v2 = int(v2)
    v2 = v2-withdr
    employee.epoints = v2
    employee.save()
    
    return HttpResponse('<h1> Withdraw Successful !!!<br><br><a href="/superuser/superlogin_index/updated"><button>Back To Main Page </button></a></h1>')