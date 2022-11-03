from django import forms
from django.core.exceptions import ValidationError

from .models import Advertisement, Response


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['heading', 'category', 'text_ad', 'upload']
        exclude = ["author"]

    def clean(self):
        cleaned_data = super().clean()
        text_ad = cleaned_data.get("text_ad")
        heading = self.cleaned_data["heading"]

        if heading[0].islower():
            raise ValidationError(
                "Заголовок должен начинаться с заглавной буквы"
            )

        if text_ad is not None and len(text_ad) < 40:
            raise ValidationError({
                "text_ad": "Текст статьи не может быть менее 40 символов."
            })

        return cleaned_data


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text_of_response', 'status']
        exclude = ['commentator', 'advertisement']


