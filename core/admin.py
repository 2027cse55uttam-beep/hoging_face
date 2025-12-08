from django.contrib import admin
from django.utils.html import format_html # <-- Ye zaroori hai icons dikhane ke liye
from .models import Contact, Project

# 1. Contact Admin (Message Readability)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Columns jo bahar dikhenge
    list_display = ('name', 'email', 'subject_colored', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
    
    # Message ko sirf Read-Only rakhein (Admin usse edit na kar paye, sirf padhe)
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

    # Custom Function: Subject ko Color dena
    def subject_colored(self, obj):
        return format_html('<b style="color: #4f46e5;">{}</b>', obj.subject)
    
    subject_colored.short_description = 'Subject'


# 2. Project Admin (Advanced Layout)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # List View: Title ke saath Icon bhi dikhega
    list_display = ('title', 'icon_preview', 'created_at')
    list_filter = ('icon', 'created_at')
    search_fields = ('title', 'description')
    list_per_page = 10
    
    # Form Layout: Jab aap edit karenge to ye sundar groups mein dikhega
    fieldsets = (
        ('Main Info', {
            'fields': ('title', 'link')
        }),
        ('Appearance & Content', {
            'fields': ('icon', 'description'),
            'classes': ('collapse',), # Is section ko click karke band/khol sakte hain
        }),
    )

    # Magic: FontAwesome Text ko Real Icon mein badalna
    def icon_preview(self, obj):
        return format_html('<i class="{}" style="font-size: 20px; color: #6366f1;"></i> &nbsp;&nbsp; {}', obj.icon, obj.get_icon_display())
    
    icon_preview.short_description = 'Icon Type'