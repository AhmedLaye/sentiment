
from django.shortcuts import render, redirect
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pickle



def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('french'))
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token.lower() not in stop_words]
    return " ".join(tokens)

def comment_view(request):
        if request.method=="POST":
                comment=request.POST.get('comment')
                
                with open('model_vectorizer.pkl', 'rb') as file:
                        loaded_model, loaded_vectorizer = pickle.load(file)
                        input_comment_preprocessed = preprocess_text(comment)
                        input_comment_vectorized = loaded_vectorizer.transform([input_comment_preprocessed])
                        prediction = loaded_model.predict(input_comment_vectorized)[0]
                        sentiment = "Positif" if prediction == 1 else "Négatif"
                        context={'comment':comment,
                                 'sentiment':sentiment
                                 }
                        


        # Affichez le formulaire ou tout autre contenu de la page d'accueil
                return render(request, 'index.html', context)  # Remplacez 'comment_form.html' par le nom de votre template
        else:
                return render(request,'index.html')
                
