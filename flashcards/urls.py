from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.topics, name='topics'),
    path('topics/', views.topics, name='topics'),
    path('flashcards/<slug:slug_topic>/', views.flashcards, name='flashcards'),
    path('word_detail/<slug:slug_flashcard>/', views.word_detail, name='word_detail'),
    path('create_topic/',views.create_topic , name ='create_topic'),
    path('create_flashcard/<slug:slug_topic>/',views.create_flashcard, name = 'create_flashcard'),
    path('success/',views.success_view,name = 'success'),
    path('topics/quiz/', views.quiz_view, name='quiz'), 
    path('hangman/', views.hangman_game, name='hangman'),
    path('delete_topic/<int:id_topic>/', views.delete_topic, name='delete_topic'),
    path('delete_flashcard/<int:id_flashcard>/', views.delete_flashcard, name='delete_flashcard'),
    path('custom_topic/<int:id_topic>/', views.custom_topic, name='custom_topic'),
    path('custom_flashcard/<int:id_flashcard>/', views.custom_flashcard, name='custom_flashcard'),
    path('register/', views.register, name='register'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)