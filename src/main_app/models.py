from django.db import models


class ContactMe(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.content[:50]}..."
