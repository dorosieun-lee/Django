from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     # 사용자로부터 입력을 받는 form 필드를 만드는 것
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        ),
    )
    # model 등록
    class Meta: # 메타 클래스라는 의미 / ModelForm 설계 구조에 맞춰서 이렇게 작성해야함
        model = Article 
        fields = '__all__' # 전체 필드를 선택한다는 의미
        # fields = ('title',)
        # exclude = ('title',)