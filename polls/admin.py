from django.contrib import admin

# Register your models here.

from .models import Question, Choice

admin.site.register(Question)
# TODO: why not also register Choice?
admin.site.register(Choice)
