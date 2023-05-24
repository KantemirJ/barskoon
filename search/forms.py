from django.forms import ModelForm, TextInput
from main.models import Ad


class AdsForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['header']