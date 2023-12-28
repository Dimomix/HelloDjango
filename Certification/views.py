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
    template_name = "form-answer.html"
    # def get(self,request):
    #     return render(request,self.template_name)

class LoginView(TemplateView):
    template_name = "pages-login.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request,username = email,password = password)
        print(1)
        if user is None:
            print(2)
            try:
                email_user = User.objects.filter(email=email).first()
                print(email_user.username)
                user = authenticate(request,username = email_user.username,password = password)
                print(3)
            except User.DoesNotExist:
                return redirect('Login')
                print(4)
        if user is not None:
            login(request,user)
            return redirect('Profile')
        else:
            return redirect('Login ')
class RegisterView(TemplateView):
    template_name = "pages-register.html"
    def get(self,request):
        form = UserCreationForm()
        return render(request,self.template_name
                    #   ,
                    #   {'form':form}
                      )
    def post(self,request):
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data['username']
        username = request.POST['login']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username,email,password)
        user.save()
        return redirect('/Login/')
class ProfileView(TemplateView):
    template_name = "pages-profile.html"
class CertificationView(TemplateView):
    template_name = "Certification.html"

# class CertificationAnswerView(TemplateView):
#     template_name = "CertificationAnswer.html"
class CertificationLevelView(TemplateView):
    template_name = "form-fileuploads.html"
class CertificationResultView(TemplateView):
    template_name = "CertificationResult.html"
class CertificationSessionView(TemplateView):
    template_name = "CertificationSession.html"
class CertificationTaskView(TemplateView):

    template_name = "CertificationTask.html"
class CompetencyView(TemplateView):
    template_name = "Competency.html"    
class SubjectView(TemplateView):
    template_name = "Subject.html"



class AddQuetions(TemplateView):
    
    template_name = 'add_quetions.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["competency"] = Competency_o.objects.all()
        context["level"] = CertificationLevel.objects.all()
        context["category"] = Category.objects.all()


        return context
    
    def post(self,request, *args, **kwargs):
        subject = request.POST.get('subject')
        category = request.POST.get('category')
        for key in request.POST:
            if key.startswith('question_'):
                try:
                    split = key.split('_')[1]
                    quetion = request.POST.get(key)
                    image = request.POST.get(f'image_{split}')
                    level = request.POST.get(f'level_{split}')
                    print(f'{image} {level} {quetion}')
                    CertificationTask(
                        content = quetion,
                        image = image,
                        сategory = Category.objects.get(name = category),
                        competency = Competency_o.objects.get(name = subject),
                        level = CertificationLevel.objects.get(level = level)
                    ).save()

                except Exception as e:
                    print(e)
        return redirect('add_quetions')

            


    