from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Competency(models.Model):
    # Компетенции, например: Педагогические, Психологические и т.д.
    name = models.CharField(max_length=100)
    # type = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
class CertificationLevel(models.Model):
    # Уровни сертификации, например: 5, 6, 7, 8
    level = models.IntegerField()
    requirements = models.TextField(blank=True,null=True)
    def __str__(self):
        return str(self.level)
class Category(models.Model):
    # Бакалавр Магистр и т.д.
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
class Teacher(models.Model):
    # Преподаватели
    user = models.OneToOneField(User, related_name='teacher', on_delete=models.CASCADE,null=True)
    # subjects = models.ManyToManyField(Subject, related_name='teachers')
    competencies = models.ManyToManyField(Competency, related_name='teachers', blank=True, null=True)
    сategory = models.ForeignKey(Category, related_name='teachers', on_delete=models.CASCADE,blank=True, null=True)
    certification_level = models.ForeignKey(CertificationLevel, related_name='teachers',blank=True,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class CertificationTask(models.Model):
    # Задачи для сертификации
    title = models.CharField(max_length=100, null = True, blank=True)
    content = models.TextField()
    competency = models.ForeignKey(Competency, related_name='tasks', on_delete=models.CASCADE)
    сategory = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE,null=True)
    # su bject = models.ForeignKey(Subject, related_name='certification_sessions', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='certification_tasks', blank=True,null=True)
    level = models.ForeignKey(CertificationLevel, related_name='tasks', blank=True,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.content
class CertificationAnswer(models.Model):
    task = models.ForeignKey(CertificationTask, related_name='answers', on_delete=models.CASCADE)
    # result = models.ForeignKey('CertificationResult', related_name='answers', on_delete=models.CASCADE)
    content = models.TextField(null=True,blank=True)
    correct = models.BooleanField(null=True,blank=True)
    ball = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.task.content
class CertificationSession(models.Model):
    # Сессии сертификации
    teacher = models.ForeignKey(Teacher, related_name='certification_sessions', on_delete=models.CASCADE)
    competency=models.ForeignKey(Competency, related_name='certification_sessions', on_delete=models.CASCADE)
    level = models.ForeignKey(CertificationLevel, related_name='certification_sessions', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    end_time=models.DateTimeField(null=True,blank=True)
    task=models.ManyToManyField(CertificationTask, related_name='certification_sessions')
    answer = models.ManyToManyField(CertificationAnswer, related_name='certification_sessions')
    score = models.IntegerField(null=True,blank=True)
    passed = models.BooleanField(null=True,blank=True, default=False) 
    def __str__(self):
        return self.teacher.user.username
class CertificationAnswerFile(models.Model):
    answer = models.ForeignKey(CertificationAnswer, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='certification_answers')
