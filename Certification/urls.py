from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('Answerpage/',CertificationAnswerView.as_view(),name = 'Answerpage'),
    path('Login/',LoginView.as_view(),name = 'Login'),
    path('Register/',RegisterView.as_view(),name = 'Register'),
    path('Profile/',ProfileView.as_view(),name = 'Profile'),
    path('Certification/',Certification.as_view(),name = 'Certification'),
    path('CertificationAnswer/',CertificationAnswer.as_view(),name = 'CertificationAnswer'),
    path('CertificationLevel/',CertificationLevel1.as_view(),name = 'CertificationLevel'),
    path('CertificationResult/',CertificationResult.as_view(),name = 'CertificationResult'),
    path('CertificationSession/',CertificationSession.as_view(),name = 'CertificationSession'),
    path('CertificationTask/',CertificationTask1.as_view(),name = 'CertificationTask'),
    path('Competency/',Competency.as_view(),name = 'Competency'),
    path('Subject/',Subject.as_view(),name = 'Subject'),
    path('add_quetions/',AddQuetions.as_view(),name = 'add_quetions'),

    # path('Profile/',Profile.as_view(),name = 'Profile'),
    
]
