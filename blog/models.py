from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Post(models.Model):
    featured_pic = models.ImageField(upload_to = "featured-image", null=True, blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete= models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    subject = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    detail = models.TextField()

    def __str__(self):
        return self.subject	