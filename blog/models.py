from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class Post(models.Model) :
    title = models.CharField(max_length=100)
    body = models.TextField()
    published = models.DateTimeField()
    slug = models.SlugField(max_length=100, blank=True)
    
    def __str__(self) :
        return self.title
        
    def get_absolute_url(self) :
        return reverse('blog.views.post_show', kwargs={'slug':self.slug})
    
class Link(models.Model) :
    url = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    published = models.DateTimeField()
    
    def __str__(self) :
        return self.url
        
def post_pre_save(signal, instance, sender, **kwargs) :
    instance.slug = slugify(instance.title)
    
signals.pre_save.connect(post_pre_save, sender=Post) 
