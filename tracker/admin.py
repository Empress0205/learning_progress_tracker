from django.contrib import admin
from . models import Subject,Goal, Progress, Reminder
# Register your models here.

admin.site.site_header = "Student Learning Tracker Admin"
admin.site.register(Subject)
admin.site.register(Goal)
admin.site.register(Progress)
admin.site.register(Reminder)
