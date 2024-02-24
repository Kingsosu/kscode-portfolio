from django.contrib import admin
from portfolioapp.models import ProjectDetails

# Register your models here.
class ProjectDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'jobtype')
    search_fields = ('name', 'descripition', 'jobtype')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(ProjectDetails, ProjectDetailsAdmin)

