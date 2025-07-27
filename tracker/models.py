from django.db import models

# Create your models here.
class Subject(models.Model): 
    name = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='subjects')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Goal(models.Model):
    description = models.TextField(blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='goals')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='goals')
    target_hours=models.FloatField()
    week_start=models.DateField()
    week_end=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False) 
    
    def __str__(self):
        return f"{self.subject.name} GoaL ({self.week_start})"
    
class Progress(models.Model):
    subject= models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='progress')
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='progress')
    date = models.DateField()
    hours_spent= models.FloatField()
    note=models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.goal.subject.name} Progress ({self.date})"
    

class Reminder(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reminders')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='reminders')
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='reminders')
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    is_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Reminder for {self.goal.subject.name} on {self.date} at {self.time}"