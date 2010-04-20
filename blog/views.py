from django.shortcuts import render_to_response
from models import Post, Link

def post_index(request) :
    posts = Post.objects.order_by('-published')
    
    return render_to_response('blog/index.html', {'posts':posts})
        
def post_show(request, post_id) :
    post = Post.objects.get(id=post_id)
    return render_to_response('blog/show.html', {'post':post})
        
def link_index(request) :
    links = Link.objects.all()
    
    return render_to_response('blog/link/index.html', {'links':links})
