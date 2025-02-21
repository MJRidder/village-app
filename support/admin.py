from django.contrib import admin
from .models import Support
# , Respond
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Support)
class SupportAdmin(SummernoteModelAdmin):

    list_display = ('topic', 'region', 'age_group', 'type_of_request', 'created_on')
    search_fields = ['topic', 'created_on', 'age_group', 'type_of_request', 'region']
    list_filter = ('status', 'age_group', 'type_of_request', 'region')
    # QUESTION - how to minimise the filters in admin?
    prepopulated_fields = {'slug': ('topic',)}
    # QUESTION - how can I make the slug unique? add parent in there?
    summernote_fields = ('content',)


# Register your models here.
# admin.site.register(Respond)
