from django.contrib import admin

# Register your models here.
from core.models import notification


class notificationAdmin(admin.ModelAdmin):
    list_display = ('id','title','body','date','link',)

admin.site.register(notification, notificationAdmin)