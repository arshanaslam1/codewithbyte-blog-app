from django.contrib import admin

from user_profile.models import UserProfile, Contact, Skills, Resume, Project


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'gender', 'phone', 'country')
    search_fields = ('country', 'address', 'about')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass
    list_display = ('category', 'user', 'name')
    list_filter = ('user',)


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass
    list_display = ('category', 'user', 'title')
    list_filter = ('user',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
    list_display = ('category', 'user', 'title')
    list_filter = ('user',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'phone', 'message', 'created_on',)
    list_filter = ('subject', 'created_on',)
    search_fields = ('email', 'message',)
