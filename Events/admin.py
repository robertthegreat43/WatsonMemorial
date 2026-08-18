from django.contrib import admin
from Events.models import Pastor, EventSales, Events, DailyBread, VideoSegments, ChatBot, LocalScripture


class PastorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class EventSalesAdmin(admin.ModelAdmin):
    list_display = ('Product', 'price')
    list_filter = ('Product',)
    search_fields = ('Product',)
    list_editable = ('price',)
    ordering = ('Product',)
    event_date = ('date_created',)


class EventsAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date')

    class Meta:
        model = Events
        ordering = ('event_date',)


class DailyBreadAdmin(admin.ModelAdmin):
    list_display = ('scripture_name', 'author')

    class Meta:
        model = DailyBread
        ordering = ('date_created',)


class VideoSegmentsAdmin(admin.ModelAdmin):
    list_display = ('video_segment',)

    class Meta:
        model = VideoSegments


class LocalScripturesAdmin(admin.ModelAdmin):
    list_display = ('topic',
                    'reference',
                    'reflection',
                    'created_at',
                    'updated_at',
                    )

    class Meta:
        model = LocalScripture


admin.site.register(Pastor, PastorAdmin)
admin.site.register(EventSales, EventSalesAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(DailyBread, DailyBreadAdmin)
admin.site.register(VideoSegments, VideoSegmentsAdmin)
admin.site.register(LocalScripture, LocalScripturesAdmin)
