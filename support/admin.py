from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Support, Respond



@admin.register(Support)
class SupportAdmin(SummernoteModelAdmin):

    list_display = (
        'status',
        'topic',
        'region',
        'age_group',
        'type_of_request',
        'created_on')
    search_fields = [
        'topic',
        'created_on',
        'age_group',
        'type_of_request',
        'region']
    list_filter = (
        'status',
        'age_group',
        'type_of_request',
        'region')
    prepopulated_fields = {'slug': ('topic',)}
    summernote_fields = ('content',)


@admin.register(Respond)
class RespondAdmin(SummernoteModelAdmin):

    list_display = ('approved', 'parent', 'created_on')
    search_fields = ['parent', 'created_on']
    list_filter = ('approved', 'parent')
    summernote_fields = ('content',)
