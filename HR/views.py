from django.http import HttpResponse
from django.shortcuts import render
from .models import Applicant_Registration,HR_Registration




def HRloginpage(request):
    type = request.GET.get('type')
    return render(request,'index.html',{'type':type})

def HRsignin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if HR_Registration.objects.filter(username=username, password=password):
        return render(request, 'applicant.html')
    else:
        return render(request, 'index.html', {'type': 'applicant_login'})


def ApplicantloginPage(request):
    type = request.GET.get('type')
    return render(request,'index.html',{'type':type})

def InterviewerloginPage(request):
    type = request.GET.get('type')
    return render(request, 'index.html', {'type': type})

def InterviewerSignup(request):
    return render(request,'interviewer.html')

def ManagerloginPage(request):
    type = request.GET.get('type')
    return render(request, 'index.html', {'type': type})

def ManagerSignin(request):
    return render(request,'manager.html')

def Applicantsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    username = request.POST.get('username')
    password = request.POST.get('pass')

    if Applicant_Registration.objects.filter(email=email):
        return render(request, 'index.html', {'type': 'applicant_login','msg':'username is already available'})
    else:
        AppReg = Applicant_Registration(name=name,email=email,phone=phone,username=username,password=password)
        AppReg.save()
        return render(request,'index.html',{'type':'applicant_login','msg':'saved successfully!'})


def Applicantsignin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if Applicant_Registration.objects.filter(username=username,password=password):
        return render(request,'applicant.html')
    else:
       return render(request, 'index.html',{'type':'applicant_login'})


