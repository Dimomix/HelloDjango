from django.db import models

# Create your models here.
class Teacher(models.Model):
    # Персональные данные учителя
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # ...

class Competency(models.Model):
    # Компетенции, например: Педагогические, Психологические и т.д.
    name = models.CharField(max_length=100)
    description = models.TextField()

class CertificationLevel(models.Model):
    # Уровни сертификации, например: 5, 6, 7, 8
    level = models.IntegerField()
    requirements = models.TextField()

class Subject(models.Model):
    # Предметы, например: Математика, Информатика и т.д.
    name = models.CharField(max_length=100)
    description = models.TextField()

class CertificationTask(models.Model):
    # Задачи для сертификации
    title = models.CharField(max_length=100)
    content = models.TextField()
    competency = models.ForeignKey(Competency, related_name='tasks', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='certification_tasks', blank=True)
    level = models.ForeignKey(CertificationLevel, related_name='tasks', on_delete=models.CASCADE)
class CertificationAnswer(models.Model):
    task = models.ForeignKey(CertificationTask, related_name='answers', on_delete=models.CASCADE)
    result = models.ForeignKey('CertificationResult', related_name='answers', on_delete=models.CASCADE)
    content = models.TextField()
    correct = models.BooleanField()
    ball = models.IntegerField()
class CertificationAnswerFile(models.Model):
    answer = models.ForeignKey(CertificationAnswer, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='certification_answers')
class CertificationResult(models.Model):
    # Результаты сертификации
    teacher = models.ForeignKey(Teacher, related_name='certification_results', on_delete=models.CASCADE)
    task = models.ForeignKey(CertificationTask, related_name='results', on_delete=models.CASCADE)
    score = models.IntegerField()
    passed = models.BooleanField()