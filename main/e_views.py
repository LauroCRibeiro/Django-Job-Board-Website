# Employee Views
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .forms import *
from django.db.models import Q
from .e_models import *
# Register
def register(request):
    if 'empLogin' in request.session:
        return redirect('/profile')
    if request.method=='POST':
        registerForm=EmployeeRegisterForm(request.POST)
        if registerForm.is_valid():
            employee=registerForm.save()
            employee.save()
            messages.success(request, 'You have registred successfully.')
            return redirect('/register')
    else:
        form=EmployeeRegisterForm()
    return render(request,'register.html',{'form':form})
# Login
def login(request):
    if 'empLogin' in request.session:
        return redirect('/profile')
    if request.method=='POST':
        loginForm=EmployeeLoginForm(request.POST)
        if loginForm.is_valid():
            email=loginForm.cleaned_data['email']
            password=loginForm.cleaned_data['password']
            check=Employee.objects.filter(email=email,password=password).count()
            if check>0:
                emp_data=Employee.objects.get(email=email,password=password)
                request.session['empLogin']=True
                request.session['empId']=emp_data.id
                if 'next' in request.GET:
                    redirect('/')
                return redirect('/profile')
            else:
                messages.info(request,'Invalid Email/Password!!')
    else:
        loginForm=EmployeeLoginForm()
    return render(request,'login.html',{'form':loginForm})
# Employee Logout
def logout(request):
    del request.session['empLogin']
    del request.session['empId']
    return redirect('/login')
# Profile
def profile(request):
    emp=get_object_or_404(Employee,id=request.session['empId'])
    if request.method=='POST':
        registerForm=EmployeeRegisterForm(request.POST,instance=emp)
        if registerForm.is_valid():
            registerForm.save()
            messages.success(request,'Profile has been updated.')
            return redirect('/profile')
    registerForm=EmployeeRegisterForm(instance=emp)
    return render(request,'profile.html',{'form':registerForm})

# Public Profile
def public_profile(request,id):
    emp=get_object_or_404(Employee,id=id,active_status=True,public=True)
    return render(request,'public-profile.html',{'emp':emp})

# Applied Jobs
def applied_jobs(request):
    emp=get_object_or_404(Employee,id=request.session['empId'])
    jobs=ApplyJob.objects.filter(employee=emp).order_by('applied_time')
    return render(request,'applied.html',{'jobs':jobs})
# Recommended Jobs
def recom_jobs(request):
    emp=get_object_or_404(Employee,id=request.session['empId'])
    jobs=Job.objects.filter(title__icontains=emp.job_title,publish=True).order_by('-id')
    return render(request,'recom.html',{'jobs':jobs})
# Messages