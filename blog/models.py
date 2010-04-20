from django.db import models

class Post(models.Model) :
    title = models.CharField(max_length=100)
    body = models.TextField()
    published = models.DateTimeField()
    
    def __str__(self) :
        return self.title
    
class Link(models.Model) :
    url = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    published = models.DateTimeField()
    
    def __str__(self) :
        return self.url
