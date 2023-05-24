from django.forms import ModelForm, Textarea
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': Textarea(attrs={
                'style': "border-radius: 10px; resize: none;",
                'cols': "158",
                'rows': "8"
            })
        }