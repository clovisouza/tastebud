from django.http import HttpResponse
from django.template import Context, loader
import settings
app = __import__("%s" % settings.MODULE_NAME,globals(),locals(),['settings'])
# app settings become app.settings.whatever
blog = __import__("%s.blog.models" % settings.MODULE_NAME,globals(),locals(),['models'])
# blog models become blog.models.BlogEntry etc etc

from datetime import datetime as d

def index(request):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))

