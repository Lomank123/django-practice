from django.contrib import admin
from testapp.models import Category, Tag, Item, Comment
import pprint
from django.contrib.sessions.models import Session


class SessionAdmin(admin.ModelAdmin):
    """
    To display sessions info in django admin.
    """

    def _session_data(self, obj):
        return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')

    _session_data.allow_tags = True
    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
    exclude = ['session_data']
    date_hierarchy = 'expire_date'


admin.site.register(Session, SessionAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Item)
admin.site.register(Comment)
