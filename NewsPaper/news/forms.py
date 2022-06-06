from django.forms import ModelForm
from .models import Post
 
 
# Создаём модельную форму
class NewsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['head_of_post', 'article_text', 'post_author', 'post_type']