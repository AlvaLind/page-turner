from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About_Us


# Register your models here.
@admin.register(About_Us)
class About_UsAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)