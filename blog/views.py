from django.http import HttpResponse
from django.template import Context, loader

# need to import the settings from the module...this sucks.  It means that
# the top module needs to be in the import path.  This is confusing.
import settings
app = __import__("%s" % settings.MODULE_NAME,globals(),locals(),['settings'])
# app settings become app.settings.whatever
blog = __import__("%s.blog.models" % settings.MODULE_NAME,globals(),locals(),['*'])
# blog models become blog.BlogEntry etc etc

from datetime import datetime as d

def standard_context():
    """ news up and returns a Context """
    c = Context({
        'site_name' :settings.SITE_NAME,
        'feed_url'  :settings.FEED_URL, 
        'title'     :settings.SITE_NAME
    })
    return c
    
def front_page(request):
    """The index of the site.  If there's a static page with the slug of main, display that, otherwise
    show the blog_latest view."""
    try:
        main_page = blog.Page.objects.get(show_on_main_page=True)
        return page(request, main_page.slug, main_page)
    except:
        return blog_latest(request)
    
def page(request,slug,page=None):
    """Display a page by slug, also has the option of passing in a page already pulled from the database."""
    c = standard_context()
    t = loader.get_template("page.html")
    if page:
        c['title'] = page.title
        c['page'] = page
        return HttpResponse(t.render(c))
    else:
        c['page'] = blog.Page.objects.all().filter(slug=slug)[0]
        c['title'] = c['page'].title
        return HttpResponse(t.render(c))
    
def blog_latest(request):
    c = standard_context()
    t = loader.get_template("blog.html")
    c['entries'] = blog.BlogEntry.objects.all().filter(date_added__lte=d.now()).order_by('-date_added')[0:9]
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
