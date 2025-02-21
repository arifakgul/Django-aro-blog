from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

# "on_delete= models.CASCADE" bu bir user silindiğinde onun tablolarınıda siler.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    title = models.CharField(max_length= 50)
    content = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add= True)
    article_image = models.FileField(blank=True, null=True, verbose_name="Makaleye Fotoğoraf Ekleyin:")
    likes = models.ManyToManyField(User, related_name="liked_article", blank=True)

    def total_likes(self):
        return self.likes.count() 

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_date"]
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.comment_author
    
    class Meta:
        ordering = ["-comment_date"]