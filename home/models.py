from django.db import models

class Comment(models.Model):
    text = models.TextField()  # Champ pour stocker le texte du commentaire
    sentiment = models.CharField(max_length=10)  # Champ pour stocker le sentiment (positif/négatif)

    def __str__(self):
        return self.text  # Renvoie le texte du commentaire comme représentation de chaîne
