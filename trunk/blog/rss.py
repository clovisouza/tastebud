from django.contrib.syndication.feeds import Feed
import settings
blog = __import__("%s.blog.models" % settings.MODULE_NAME,globals(),locals(),['views'])
from datetime import datetime as d

class BlogFeed(Feed):
    title = settings.SITE_NAME
    link = "/"
    description = settings.SITE_DESCRIPTION

    def items(self):
        return blog.BlogEntry.objects.filter(date_added__lte=d.now()).order_by('-date_added')[:10]
    
    def item_author_name(self, item):
        """This doesn't seem to work"""
        #r = ""
        #for author in item.authors:
        #    r = "%s %s " % (r,author)
        #return r
        return item.authors
    
    def item_link(self, item):
        return item.get_absolute_url()
    
    def item_pubdate(self, item):
        return item.date_added
