from django.contrib import admin
from .models import Project, ProjectImage, Comment

# Customize Project admin
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Number of empty image fields to display

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')  # Include category
    list_filter = ('category', 'created_at')  # Filter by category and creation date
    search_fields = ('title', 'description', 'category')  # Searchable fields
    inlines = [ProjectImageInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image', 'category')  # Add category here
        }),
        ('Details', {
            'fields': ('technologies_used', 'issues_faced'),
            'classes': ('collapse',)
        }),
    )

# Register models with the admin
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Comment)
