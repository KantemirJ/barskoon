from django.forms import ModelForm, Textarea
from .models import CommentPerson


class CommentPersonForm(ModelForm):
    class Meta:
        model = CommentPerson
        fields = ['comment']
        widgets = {
            'comment': Textarea(attrs={
                'style': "border-radius: 10px; resize: none;",
                'cols': "158",
                'rows': "8"
            })
        }