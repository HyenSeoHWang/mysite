'''
* 장고 관리자 기능 URL
* https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
'''
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']

admin.site.register(Question, QuestionAdmin)

