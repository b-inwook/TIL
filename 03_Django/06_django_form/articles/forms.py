from django import forms
from .models import Article, Comment

#--------------------------------------------------------#
# 아래는 modelform을 사용했을 때,
class ArticleForm(forms.ModelForm):
    # model의 정보 Meta 정보로 만듬
    # 즉, model에서  동일한 article 클래스로 사용할 것.
    # 가장 중요하고, modelForm을 사용해야한다.

    # 방법 2.

    title = forms.CharField(
        max_length=10,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        )
    )
    class Meta:
        model = Article
        fields = ('title', 'content',)

        # 방법1.

        # Meta widgets는 주석처리하고, 위에 따로 widget을 만드는 방법도 있다.
        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'class': 'my-title',
        #             'placeholder': 'Enter the title!',
        #         }
        #     )
        # }


#--------------------------------------------------------#
# 아래는 form만 사용했을 때,

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=20,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'my-title',
#                 'placeholder': 'Enter the title!',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             # 속성값
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': 'Enter the content!',
#                 'rows': 5,
#                 'cols': 50,
#             }
#         )
#     )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)