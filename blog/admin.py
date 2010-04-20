from django.contrib import admin
from models import Post, Link

class PostAdmin(admin.ModelAdmin) :
    class Media:
        js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
        
class LinkAdmin(admin.ModelAdmin) :
    class Media:
        js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 
        
admin.site.register(Post, PostAdmin)
admin.site.register(Link, LinkAdmin)

