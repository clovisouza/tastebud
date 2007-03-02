from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='images/photos', height_field='height', width_field='width',)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return "%s %s" % (self.caption, self.image)
        
    def show(self):
        return "<img src=\"%s\" height=%i width=%i alt=\"%s\">" % (self.get_image_url(), self.height, self.width, self.caption)
        
    class Admin:
        fields = (
            (None, {
                'fields': ('image', 'caption')
            }),
            )
    
    class Meta:
        ordering = ['caption']
        
class Podcast(models.Model):
    data = models.FileField(upload_to='podcasts')
    title = models.CharField(maxlength=255)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Admin:
        pass
        
class BlogEntry(models.Model):
    title = models.CharField(maxlength=255)
    date_added = models.DateField()
    body = models.TextField()
    photo = models.ForeignKey(Photo, blank=True, null=True)
    podcast = models.ForeignKey(Podcast, blank=True, null=True)
    slug = models.SlugField(prepopulate_from=('title',))
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "http://tastebudchicago.com/blog/%s" % self.slug

    class Admin:
        pass
        


