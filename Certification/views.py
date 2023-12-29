from django.shortcuts import render, redirect,reverse
from django.views.generic import TemplateView
from Certification.models import CertificationAnswer, Teacher

from django.http import JsonResponse
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
from django.core import serializers
from datetime import datetime, timedelta
import random
# Create your views here.
class CertificationAnswerView(TemplateView):
    # template_name = "form-answer.html"
    template_name ="form-fileuploads.html"
    def get(self,request):
        user=request.user
        teacher = Teacher.objects.filter(user=user).first()
        session=CertificationSession.objects.filter(teacher=teacher,passed=False).first()
        answer=session.answer.first()
        context={
            'answer':answer,
            'session':session
        }
        return render(request,self.template_name,context)
def answer_detail(request, pk):
    if request.method == 'POST':
        answer = CertificationAnswer.objects.get(pk=pk)
        # answer.content=request.POST['answer']
        content = request.POST.get('content')
        files = request.FILES.get('file')
        answer.content=content
        answer.save()
        print(content)
        print(files)
        if files:
            file=CertificationAnswerFile.objects.create(file=files)
            file.save()
            
        return redirect('CertificationAnswer')
    answer = CertificationAnswer.objects.get(pk=pk)
    user=request.user
    teacher = Teacher.objects.filter(user=user).first()
    session=CertificationSession.objects.filter(teacher=teacher,passed=False).first()
    context={
        'answer':answer,
        'session':session
    }
    # Дополнительная логика, если нужно
    return render(request, "form-fileuploads.html", context)
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
        teacher = Teacher.objects.create(user=user)
        user.save()
        return redirect('Login')
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


def get_random_tasks(level, count=10):
    # Получаем задачи с определенным уровнем
    tasks_with_level = CertificationTask.objects.filter(level=level)

    # Получаем случайные задачи из этого набора
    random_tasks = random.sample(list(tasks_with_level), min(count, len(tasks_with_level)))

    return random_tasks

class CertificationSessionView(TemplateView):
    template_name = "session.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["competency"] = Competency.objects.all()
        context["category"] = Category.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        category = request.POST.get('category')
        competency = request.POST.get('competency')
        session = CertificationSession(
            teacher = Teacher.objects.get(user = self.request.user),
            competency = Competency.objects.get(name = competency),
            category = Category.objects.get(name = category),
            end_time = datetime.now() + timedelta(hours=1),
        )
        random_tasks = get_random_tasks(Category.objects.get(name = category).level)  # Используем функцию, описанную ранее
        for task in random_tasks:
            session.task.add(task)
            ans = CertificationAnswer.objects.create(task = task)
            session.answer.add(ans)

        session.save()
        return redirect('CertificationSession')


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

        context["competency"] = Competency.objects.all()
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
                        competency = Competency.objects.get(name = subject),
                        level = CertificationLevel.objects.get(level = level)
                    ).save()
                   

                except Exception as e:
                    print(e)
        return redirect('add_quetions')

            

def certification_task_list(request):
    tasks = CertificationTask.objects.all().values(
        'id', 'title', 'content', 
        'competency__name', 'сategory__name', 'image', 'level__level'
    )
    task_list = list(tasks)  # Преобразование QuerySet в список
    return JsonResponse(task_list, safe=False)


def delete_question(request, question_id):

    try:
            question = CertificationTask.objects.get(id=int(question_id))
            question.delete()
            return JsonResponse({'status': 'success', 'message': 'Вопрос удален'})
    except CertificationTask.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Вопрос не найден'}, status=404)

