from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.comments.models import FreeComment

import settings
app = __import__("%s" % settings.MODULE_NAME,globals(),locals(),['settings'])
# app settings become app.settings.whatever
blog = __import__("%s.blog.models" % settings.MODULE_NAME,globals(),locals(),['*'])
# blog models become blog.BlogEntry etc etc

from datetime import datetime as d

def standard_context():
    """ news up and returns a Context """
    c = Context({'site_name':app.settings.SITE_NAME,'feed_url':app.settings.FEED_URL})
    return c
    
def blog_latest(request):
    c = standard_context()
    t = loader.get_template("blog.html")
    c['entries'] = blog.BlogEntry.objects.all().filter(date_added__lte=d.now()).order_by('date_added')[0:9]
    return HttpResponse(t.render(c))

def blog_archive(request):
    c = standard_context()
    t = loader.get_template("blog_archive.html")
    c['entries'] = blog.BlogEntry.objects.all().filter(date_added__lte=d.now()).order_by('-date_added')
    return HttpResponse(t.render(c))
    
def blog_entry(request, slug):
    c = standard_context()
    t = loader.get_template("blog.html")
    c['entries'] = blog.BlogEntry.objects.filter(slug=slug)
    c['title'] = c['entries'][0].title
    return HttpResponse(t.render(c))
    
def category_listing(request, slug):
    c = standard_context()
    t = loader.get_template("category.html")
    c['category'] = blog.Category.objects.filter(slug=slug)[0]
    c['entries'] = blog.BlogEntry.objects.filter(categories__slug__exact=slug)
    c['title'] = c['category'].name
    return HttpResponse(t.render(c))
