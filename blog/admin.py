from django.contrib import admin
from models import Post

class PostAdmin(admin.ModelAdmin) :
    class Media:
        js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
        
admin.site.register(Post, PostAdmin)

