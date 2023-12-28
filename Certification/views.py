from django.shortcuts import render, redirect,reverse
from django.views.generic import TemplateView
from Certification.models import CertificationAnswer


import django.shortcuts
from django.views.generic import TemplateView
from django.contrib import messages  # Импортируем messages для отправки сообщений пользователю
# from .form import RegisterForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout
from requests.exceptions import HTTPError
from django.http import HttpResponse
# Create your views here.
class CertificationAnswerView(TemplateView):
    template_name = "form-fileuploads.html"
    

class LoginView(TemplateView):
    template_name = "pages-login.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('/Profile/')
        else:
            return redirect('/login/')
class RegisterView(TemplateView):
    template_name = "pages-register.html"
    def get(self,request):
        form = UserCreationForm()
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
class ProfileView(TemplateView):
    template_name = "Profile.html"
class Certification(TemplateView):
    template_name = "Certification.html"
class CertificationAnswer(TemplateView):
    template_name = "CertificationAnswer.html"
class CertificationLevel(TemplateView):
    template_name = "CertificationLevel.html"
class CertificationResult(TemplateView):
    template_name = "CertificationResult.html"
class CertificationSession(TemplateView):
    template_name = "CertificationSession.html"
class CertificationTask(TemplateView):
    template_name = "CertificationTask.html"
class Competency(TemplateView):
    template_name = "Competency.html"    
class Subject(TemplateView):
    template_name = "Subject.html"

    