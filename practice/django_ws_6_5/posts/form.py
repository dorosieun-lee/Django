from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'content': forms.Textarea(attrs= {
                'rows': 6,
                'cols': 100,
            })
        }