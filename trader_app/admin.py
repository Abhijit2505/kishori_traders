from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.

@admin.register(scope_of_work)
class ScopeOfWorkAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
    
admin.site.register(jobRegister)
admin.site.register(WindingData)
admin.site.register(TestReport)