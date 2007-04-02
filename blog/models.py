from django.db import models
from django.contrib.sites.models import Site

class Author(models.Model):
    """Authors are included fields in both articles and photos"""
    name = models.CharField(maxlength=255,)
    about = models.TextField(blank=True)
    homepage = models.URLField(blank=True, null=True)
    slug = models.SlugField(prepopulate_from=('name',))
    
    def has_articles(self):
        """returns true if there are articles to their credit"""
        if self.article_set.all().count() > 0:
            return True
        return False
    
    def has_photos(self):
        """returns true if there are photos to their credit"""
        if self.photo_set.all().count() > 0:
            return True
        return False
    
    def get_absolute_url(self):
        """html link to authors page"""
        return "<a href=\"/authors/%s\">%s</a>" % (self.slug, self.name)
    
    def __str__(self):
        return self.name

    class Admin:
        pass
        
class Photo(models.Model):
    image = models.ImageField(upload_to='images', height_field='height', width_field='width',)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    credit = models.ManyToManyField(Author)
    
    def __str__(self):
        return "%s %s" % (self.caption, self.image)
        
    def get_absolute_url(self):
        site = Site.objects.get_current().domain
        return "http://%s/%s" % (site,self.get_image_url())
        
    def show(self):
        return "<img src=\"%s\" height=%i width=%i alt=\"%s\">" % (self.get_absolute_url(), self.height, self.width, self.caption)
        
    class Admin:
        fields = (
            (None, {
                'fields': ('image', 'caption', 'credit')
            }),
            )
    
    class Meta:
        ordering = ['caption']
        
class Podcast(models.Model):
    filename = models.CharField(maxlength=255)
    title = models.CharField(maxlength=255)
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        site = Site.objects.get_current().domain
        return "http://%s/%s/%s" % (site,settings.PODCAST_BASE,self.filename)
    
    def link(self):
        return "<a href=\"%s\">%s</a>" % (self.get_absolute_url(), self.title)

    def __str__(self):
        return self.title
    
    class Admin:
        pass
        
class Category(models.Model):
    name = models.CharField(maxlength=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(prepopulate_from=('name',))
    
    def get_absolute_url(self):
        site = Site.objects.get_current().domain
        return "http://%s/category/%s" % (site, self.slug)
        
    def __str__(self):
        return self.name
        
    def link(self):
        return "<a href=\"%s\">%s</a>" % (self.get_absolute_url(), self.name)
    
    class Admin:
        pass
    
class BlogEntry(models.Model):
    title = models.CharField(maxlength=255)
    authors = models.ManyToManyField(Author)
    date_added = models.DateField()
    body = models.TextField()
    photo = models.ForeignKey(Photo, blank=True, null=True)
    podcast = models.ForeignKey(Podcast, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(prepopulate_from=('title',))
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        site = Site.objects.get_current().domain
        return "http://%s/blog/%s" % (site, self.slug)

    class Admin:
        pass
        


