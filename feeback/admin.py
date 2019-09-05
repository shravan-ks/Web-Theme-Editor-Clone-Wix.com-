from django.contrib import admin

# Register your models here.
from feeback.models import feedbackform


class feedbackformAdmin(admin.ModelAdmin):
    list_display = ('id','Created','user','Subject',)

admin.site.register(feedbackform, feedbackformAdmin)