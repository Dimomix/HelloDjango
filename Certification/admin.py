from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Competency)
admin.site.register(CertificationLevel)
admin.site.register(Subject)
admin.site.register(CertificationTask)