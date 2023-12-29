from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('Answerpage/',CertificationAnswerView.as_view(),name = 'Answerpage'),
    path('answer/<int:pk>/', answer_detail, name='answer_detail'),
    path('passed/<int:pk>/', passed_session, name='passed_session'),
    path('Login/',LoginView.as_view(),name = 'Login'),
    path('Register/',RegisterView.as_view(),name = 'Register'),
    path('Logout/',LogoutView.as_view(),name = 'Logout'),
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
    path('AddQuetions/', AddQuetions.as_view(),name  = 'add_quetions'),
    path('api/certification-tasks/', certification_task_list, name='certification_task_list'),
    path('delete-question/<int:question_id>/', delete_question, name='delete_question'),
]
