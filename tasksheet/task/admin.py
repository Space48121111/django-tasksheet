from django.contrib import admin

from .models import Room, Status
# Register your models here.

# class StatusInline(admin.StackedInline):
# tabular/collapsible version
class StatusInline(admin.TabularInline):

    model = Status
    # 3 more slots for each addition
    extra = 3


class RoomAdmin(admin.ModelAdmin):
    # tuple(title, field)
    fieldsets = [(None, {'fields': ['room_text']}),
    ('Date_information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    list_display = ('room_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    # LIKE query behind the scenes
    search_fields = ['room_text']
    # pagination
    list_per_page = 10

    # multiple inputs
    inlines = [StatusInline]

admin.site.register(Room, RoomAdmin)
# admin.site.register(Status)








# end
