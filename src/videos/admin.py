from django.contrib import admin

# Register your models here.
from .models import VideoAllProxy, VideoPublishedProxy


class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['title','id', 'video_id', 'is_published']
    search_fields = ['title']
    list_filter = ['active']
    readonly_fields = ['id','is_published']

    class Meta:
        model = VideoAllProxy

    # def published(self, obj, *args, **kwargs):
    #     return obj.active


admin.site.register(VideoAllProxy, VideoAllAdmin)


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    search_fields = ['title']
    # list_filter = ['video_id']

    class Meta:
        model = VideoAllProxy

    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)


admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)
