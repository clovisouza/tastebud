from django.http import HttpResponse
from django.template import Context, loader
import settings
app = __import__("%s" % settings.MODULE_NAME,globals(),locals(),['settings'])
# app settings become app.settings.whatever
blog = __import__("%s.blog.models" % settings.MODULE_NAME,globals(),locals(),['models'])
# blog models become blog.models.BlogEntry etc etc

from datetime import datetime as d

def standard_context():
    """ news up and returns a Context """
    c = Context({'site_name':app.settings.SITE_NAME,'feed_url':app.settings.FEED_URL})
    return c
    
def index(request):
    t = loader.get_template("index.html")
    c = standard_context()
    return HttpResponse(t.render(c))

