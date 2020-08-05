from django.db import models


# Create a Blog model
class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
