from django import forms
from articles.models import Article

class ArticleForm(forms.ModelForm):
    # meta 클래스
    class Meta:
        model = Article
        fields = '__all__' # Article의 모든 fields를 form으로 만들어라
        # exclude = ('title',)

# class ArticleForm(forms.Form):
#     REGION_A = "sl"
#     REGION_B = "dj"
#     REGION_C = "gj"
#     REGION_D = "gm"
#     REGION_E = "bu"
#     REGION_CHOICES = [
#         (REGION_A, '서울'),
#         (REGION_B, '대전'),
#         (REGION_C, '광주'),
#         (REGION_D, '구미'),
#         (REGION_E, '부산'),
#     ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select())
