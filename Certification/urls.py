from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('Answerpage/',CertificationAnswerView.as_view(),name = 'Answerpage'),
    path('answer/<int:pk>/', answer_detail, name='answer_detail'),
    path('Login/',LoginView.as_view(),name = 'Login'),
    path('Register/',RegisterView.as_view(),name = 'Register'),
    path('Profile/',ProfileView.as_view(),name = 'Profile'),
    path('Certification/',CertificationView.as_view(),name = 'Certification'),
    path('CertificationAnswer/',CertificationAnswerView.as_view(),name = 'CertificationAnswer'),
    path('CertificationLevel/',CertificationLevelView.as_view(),name = 'CertificationLevel'),
    path('CertificationResult/',CertificationResultView.as_view(),name = 'CertificationResult'),
    path('CertificationSession/',CertificationSessionView.as_view(),name = 'CertificationSession'),
    path('CertificationTask/',CertificationTaskView.as_view(),name = 'CertificationTask'),
    path('Competency/',CompetencyView.as_view(),name = 'Competency'),
    path('Subject/',SubjectView.as_view(),name = 'Subject'),
    # path('Profile/',Profile.as_view(),name = 'Profile'),
    
]
