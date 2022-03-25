from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Document(models.Model):

    # Makes it so that each Document has a user. These will be accessed like this:
    # User.objects.get(username="bob331").document_set
    # To get a specific Document:
    # Document.objects.get(user__username="bob331", title="emails")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    content = models.TextField()

    def __str__(self):
        return f"Document: {self.title}"
