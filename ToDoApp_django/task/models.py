from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)
    class Meta:
        abstract=True # emphasizes that this is a Base Model. Thus when migrating, it won't generate a table

class Todo(BaseModel):
    name=models.CharField(max_length=100)
    isCompleted=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_todos")
