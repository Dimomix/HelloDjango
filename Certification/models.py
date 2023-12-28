from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Competency(models.Model):
    # Компетенции, например: Педагогические, Психологические и т.д.
    name = models.CharField(max_length=100)
    # type = models.CharField(max_length=100)
    description = models.TextField()

class CertificationLevel(models.Model):
    # Уровни сертификации, например: 5, 6, 7, 8
    level = models.IntegerField()
    requirements = models.TextField()

class Category(models.Model):
    # Бакалавр Магистр и т.д.
    name = models.CharField(max_length=100)
    description = models.TextField()

class Teacher(models.Model):
    # Преподаватели
    user = models.OneToOneField(User, related_name='teacher', on_delete=models.CASCADE,null=True)
    # subjects = models.ManyToManyField(Subject, related_name='teachers')

    competencies = models.ManyToManyField(Competency, related_name='teachers', blank=True)
    сategory = models.ForeignKey(Category, related_name='teachers', on_delete=models.CASCADE, null=True)
    certification_level = models.ForeignKey(CertificationLevel, related_name='teachers',null=True, on_delete=models.CASCADE)
    

class CertificationTask(models.Model):
    # Задачи для сертификации
    title = models.CharField(max_length=100, null = True)
    content = models.TextField()
    competency = models.ForeignKey(Competency, related_name='tasks', on_delete=models.CASCADE)
    сategory = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE,null=True)
    # su bject = models.ForeignKey(Subject, related_name='certification_sessions', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='certification_tasks', blank=True)
    level = models.ForeignKey(CertificationLevel, related_name='tasks', on_delete=models.CASCADE)
class CertificationAnswer(models.Model):
    task = models.ForeignKey(CertificationTask, related_name='answers', on_delete=models.CASCADE)
    # result = models.ForeignKey('CertificationResult', related_name='answers', on_delete=models.CASCADE)
    content = models.TextField()
    correct = models.BooleanField()
    ball = models.IntegerField()
class CertificationSession(models.Model):
    # Сессии сертификации
    teacher = models.ForeignKey(Teacher, related_name='certification_sessions', on_delete=models.CASCADE)

    competency=models.ForeignKey(Competency, related_name='certification_sessions', on_delete=models.CASCADE)
    level = models.ForeignKey(CertificationLevel, related_name='certification_sessions', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    task=models.ManyToManyField(CertificationTask, related_name='certification_sessions')
    answer = models.ManyToManyField(CertificationAnswer, related_name='certification_sessions')
    
class CertificationAnswerFile(models.Model):
    answer = models.ForeignKey(CertificationAnswer, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='certification_answers')
class CertificationResult(models.Model):
    # Результаты сертификации
    teacher = models.ForeignKey(Teacher, related_name='certification_results', on_delete=models.CASCADE)
    session=models.OneToOneField(CertificationSession, related_name='certification_results', on_delete=models.CASCADE, null = True)
    score = models.IntegerField()
    passed = models.BooleanField() 