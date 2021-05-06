from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=35)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    website = models.URLField()
    added_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    added_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.DO_NOTHING)
    pub_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


