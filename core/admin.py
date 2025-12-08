from django.contrib import admin
from .models import Contact, Project  # Dono models import karein

# 1. Contact Admin Configuration
# (Agar ye pehle se registered hai to error dega, isliye hum ek baar hi likhenge)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

# 2. Project Admin Configuration
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'created_at')
    list_filter = ('icon',)
    search_fields = ('title', 'description')

# 3. Registration (Ye sabse important part hai)
# Dhyan dein: Yahan hum check kar rahe hain taaki duplicate error na aaye
admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)