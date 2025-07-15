from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Faq


@admin.register(Faq)
class FaqAdmin(SummernoteModelAdmin):

    list_display = (
        'question',
        'region',
        'age_group',)
    search_fields = [
        'question',
        'age_group',
        'region']
    list_filter = (
        'question',
        'age_group',
        'region')
    prepopulated_fields = {'slug': ('question',)}
    summernote_fields = ('answer',)
