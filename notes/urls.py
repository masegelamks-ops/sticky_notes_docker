from django.urls import path
from . import views

# Optional: Add a namespace for your app
app_name = 'notes'

urlpatterns = [
    # ex: /notes/
    path('', views.note_list, name='note_list'),

    # ex: /notes/create/
    path('create/', views.note_create, name='note_create'),

    # ex: /notes/5/update/
    path('<int:note_id>/update/', views.note_update, name='note_update'),

    # ex: /notes/5/delete/
    path('<int:note_id>/delete/', views.note_delete, name='note_delete'),
]
