from django.contrib import admin
from .models import Topic, Flashcards, User, Study

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id_topic','name_topic')

class FlashcardsAdmin(admin.ModelAdmin):
    list_display = ('id_flashcard','front','back')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'username')

class StudyAdmin(admin.ModelAdmin):
    list_display = ('id_study', 'start_time', 'end_time', 'id_user')

# Register your models here.
admin.site.register(Topic,TopicAdmin)
admin.site.register(Flashcards,FlashcardsAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Study, StudyAdmin)