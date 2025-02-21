from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "article_image"]

        labels = {
            "title": "Başlık:",
            "content": "İçerik:",
        }

        help_texts = {
            "title": "Lütfen makalenizin başlığını girin.",
            "content": "Makale içeriğini buraya yazın.",
        }