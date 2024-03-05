from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget
# Register your models here.

@admin.register(scope_of_work)
class ScopeOfWorkAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()}
    }

@admin.register(InspectionReport)
class InspectionReportAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()}
    }

@admin.register(TestReport)
class TestReportAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()}
    }

@admin.register(TestReportDocument)
class TestReportDocumentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()}
    }


admin.site.register(jobRegister)
admin.site.register(WindingData)
admin.site.register(Quotation)