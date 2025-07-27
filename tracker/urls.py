from django.urls import path
from . views import SubjectListView, SubjectDetailView ,GoalListView, GoalDetailView ,ProgressListView, ProgressDetailView, ReminderListView, ReminderDetailView

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject'),
    path('goals/', GoalListView.as_view(), name='goal-list'),
    path('goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),
    path('progress/', ProgressListView.as_view(), name='progress-list'),
    path('progress/<int:pk>/', ProgressDetailView.as_view(), name='progress-detail'),
    path('reminders/', ReminderListView.as_view(), name='reminder-list'),
    path('reminders/<int:pk>/', ReminderDetailView.as_view(), name='reminder-detail'),

]