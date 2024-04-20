from django.db import models

class Task(models.Model):
    task = models.CharField(max_length = 200)
    is_completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_formatted_date(self):
        return self.created_at.strftime("%B %d, %Y %I:%M %p")

    def __str__(self):
        return f"{self.task} - [{self.get_formatted_date()}]"
    

# Create your models here.
