from . serializers import SubjectSerializer, GoalSerializer, ProgressSerializer, ReminderSerializer
from .models import Subject, Goal, Progress, Reminder
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from django.contrib.auth.models import User

# Create your views here.

class SubjectListView(APIView):
    def get(self, request):
        subjects = Subject.objects.filter(user=request.user)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubjectDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        subject = get_object_or_404(Subject, pk=pk, user=request.user)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        subject = get_object_or_404(Subject, pk=pk, user=request.user)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        subject = get_object_or_404(Subject, pk=pk, user=request.user)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class GoalListView(APIView):
    def get(self, request):
        goals = Goal.objects.filter(goal_user=request.user)
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GoalDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        goal = get_object_or_404(Goal, pk=pk, user=request.user)
        serializer = GoalSerializer(goal)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        goal = get_object_or_404(Goal, pk=pk, user=request.user)
        serializer = GoalSerializer(goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        goal = get_object_or_404(Goal, pk=pk, user=request.user)
        goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MarkGoalCompleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            goal = Goal.objects.get(pk=pk, user=request.user)
            goal.completed = True
            goal.save()
            return Response({'message': 'Goal marked as complete.'}, status=status.HTTP_200_OK)
        except Goal.DoesNotExist:
            return Response({'error': 'Goal not found.'}, status=status.HTTP_404_NOT_FOUND)
    

class ProgressListView(APIView):
    def get(self, request):
        progress = Progress.objects.filter(user=request.user)
        serializer = ProgressSerializer(progress, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProgressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProgressDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        progress = get_object_or_404(Progress, pk=pk, user=request.user)
        serializer = ProgressSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        progress = get_object_or_404(Progress, pk=pk, user=request.user)
        serializer = ProgressSerializer(progress, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        progress = get_object_or_404(Progress, pk=pk, user=request.user)
        progress.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ReminderListView(APIView):
    def get(self, request):
        reminders = Reminder.objects.filter(user=request.user)
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReminderDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
        serializer = ReminderSerializer(reminder)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
        serializer = ReminderSerializer(reminder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
        reminder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

