from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Teacher)

admin.site.register(Competency)
admin.site.register(Category)
admin.site.register(CertificationLevel)
# admin.site.register(Subject)
admin.site.register(CertificationTask)
admin.site.register(CertificationAnswer)
admin.site.register(CertificationSession)
admin.site.register(CertificationAnswerFile)
admin.site.register(CertificationResult)
