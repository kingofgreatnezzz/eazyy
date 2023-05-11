from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from halls.models import *
from django.contrib import auth ,messages
from django.contrib.auth import forms
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404
from django.conf import settings




def index(request):
    hm_picz = home_img.objects.all()
    return render(request,  'projects/index.html')


# Create your views here 
#login page
def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request, 'Welcome to Eazyskul '+user.username)
                return redirect('index') 
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
        else:
            return render(request, 'registration/login.html', {})


#register function 
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    user_form = UserRegistrationForm(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already taken or Invalid ')
                    return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email, password=password)
                user.save()
                messages.success(request, 'Registered successfully you can now log in')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')  
            return redirect('signup') 
    else:
        user_form = UserRegistrationForm()
    return render(request,'registration/signup.html',{'user_form': user_form})





#exam page
@login_required(login_url = 'login')
def exam(request):

    if request.method == 'POST':
        exform = examzForm(request.POST)
        if exform.is_valid():
            exform.save()
            subject = "Eazyskul  Contact request"
            body = {
                 'name' : exform.cleaned_data['name'],
                 'email' :exform.cleaned_data['email'],
                 'reg_no' : exform.cleaned_data['reg_no'],
                 'department' : exform.cleaned_data['department'],
                 'description' : exform.cleaned_data['description'] ,
                 'school' : exform.cleaned_data['school'] ,
             }
            message = "\n\n" .join(body.values())

            try:
                send_mail(subject, message ,settings.EMAIL_HOST_USER, ['kingofgreatnezzz@gmail.com'])
            except BadHeaderError:
                return HttpResponse('invalid header found')
            messages.success(request,"Request sent.You'll get a response in not less than 24 hours. Please check your mails to avoid missing communication. Thanks")
            return render(request, "projects/exam.html", {'exform': exform})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, exform.errors)
    else: 
        exform = examzForm()
           
    return render(request,"projects/exam.html", {
        "exform": exform,
    }) 

#contactz_form function 
@login_required(login_url = 'login')
def contact(request):
    if request.method == 'POST':
        contformz = ContactzForm(request.POST)
        if contformz.is_valid():
            contformz.save()
            subject = "Eazyskul  Contact request"
            body = {
                 'name' : exform.cleaned_data['name'],
                 'email' :exform.cleaned_data['email'],
                 'reg_no' : exform.cleaned_data['reg_no'],
                 'department' : exform.cleaned_data['department'],
                 'description' : exform.cleaned_data['description'] ,
                 'school' : exform.cleaned_data['school'] ,
             }
            message = "\n\n" .join(body.values())

            try:
                send_mail(subject, message ,settings.EMAIL_HOST_USER, ['kingofgreatnezzz@gmail.com'])
            except BadHeaderError:
                return HttpResponse('invalid header found')
            messages.success(request,"Request sent.You'll get a response in not less than 24 hours. Please check your mails to avoid missing communication. Thanks")
            return render(request, "projects/contact.html", {'contformz': contformz})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, contformz.errors)
    else: 
        contformz = ContactzForm()
            

    return render(request,"projects/contact.html", {
        "contformz": contformz, 
        })

#project page
@login_required(login_url = 'login')
def project(request):
    if request.method == 'POST':
        profom = GroupFormProject(request.POST)
        if profom.is_valid():
            profom.save()
            subject = "Eazyskul Project request"
            body = {
                 'name' : profom.cleaned_data['name'],
                 'email' :profom.cleaned_data['email'],
                 'regno' : profom.cleaned_data['regno'],
                 'message' : profom.cleaned_data['message'],
                 'phone' : profom.cleaned_data['phone'],
                 'department' : profom.cleaned_data['department'],
                 'project_topic' : profom.cleaned_data['project_topic'] ,
                 'school' : profom.cleaned_data['school'] ,
             }
            message = "\n\n" .join(body.values())

            try:
                send_mail(subject, message ,settings.EMAIL_HOST_USER, ['kingofgreatnezzz@gmail.com'])
            except BadHeaderError:
                return HttpResponse('invalid header found')
            messages.success(request,"Request sent.You'll get a response in not less than 24 hours. Please check your mails to avoid missing communication. Thanks")
            return render(request, "projects/project.html", {'profom': profom})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, profom.errors)
    else: 
        profom = GroupFormProject()
            
    return render(request,"projects/project.html", {
        "profom": profom, 
        })    

#about page
def about(request):
    abt1 = about_picz_memebers.objects.all()
    return render(request, "projects/about.html", {
        "abt1": abt1
    })

#work  (EAZY SKULL) page  AT  
@login_required(login_url = 'login')
def work(request):
    work1 = workz.objects.all()

    return render(request,"projects/work.html", {
        "work1" : work1
    })

# pd page 
@login_required(login_url = 'login')
def PD(request):
    pd1= pd.objects.all()
    return render(request,"projects/PD.html",{
        "pd1" :pd1
    })

def terms_condition(request):
    return render(request, 'projects/terms_condition.html')