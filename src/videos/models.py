from django.db import models
 
# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True,null=True)
    slug = models.SlugField(blank=True,null=True) # 'this-is-my-video'
    video_id = models.CharField(max_length=220)
    active = models.BooleanField(default=True)
    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # state = models.CharField(max_length=200)
    # publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False)

    @property
    def is_published(self):
        return self.active

class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name='All Video'
        verbose_name_plural='All Videos'
        

class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name='Published Video'
        verbose_name_plural='Published Videos'