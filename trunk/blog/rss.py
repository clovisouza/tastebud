from django.contrib.syndication.feeds import Feed
import settings
blog = __import__("%s.blog.models" % settings.MODULE_NAME,globals(),locals(),['views'])
from datetime import datetime as d

class BlogFeed(Feed):
    title = settings.SITE_TITLE
    link = "/blog/"
    description = settings.SITE_DESCRIPTION

    def items(self):
        return blog.BlogEntry.objects.filter(date_added__lte=d.now()).order_by('-date_added')[:10]
