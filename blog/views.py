from django.shortcuts import render_to_response
from models import Post, Link
from django.template import RequestContext 

def post_index(request) :
    posts = Post.objects.order_by('-published')
    
    return render_to_response('blog/index.html', {'posts':posts}, context_instance = RequestContext(request))
        
def post_show(request, slug) :
    post = Post.objects.get(slug=slug)
    return render_to_response('blog/show.html', {'post':post}, context_instance = RequestContext(request))
        
def link_index(request) :
    links = Link.objects.all()
    
    return render_to_response('blog/link/index.html', {'links':links}, context_instance = RequestContext(request))
