
from django.shortcuts import render, redirect

def comment_view(request):
   
        # Affichez le formulaire ou tout autre contenu de la page d'accueil
        return render(request, 'index.html')  # Remplacez 'comment_form.html' par le nom de votre template
