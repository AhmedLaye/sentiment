from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'sentiment')  # Champs à afficher dans la liste des commentaires

# Enregistrez le modèle Comment avec sa classe d'administration
admin.site.register(Comment, CommentAdmin)
