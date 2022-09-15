from pyexpat import model
from django.db import models
from django.contrib.auth import settings


User = settings.AUTH_USER_MODEL
class Todo(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_todo")
  title = models.CharField(max_length=150)
  description = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  completed = models.BooleanField()
  
  class Meta:
    ordering = ["completed"]
  
  def __str__(self):
    return self.title
