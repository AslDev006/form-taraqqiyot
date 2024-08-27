from django import forms
from .models import Leeds
from phonenumber_field.formfields import PhoneNumberField



class LeedsForm(forms.ModelForm):
    class Meta:
        model = Leeds
        fields = "__all__"


class LeedsFormUpdateForm(forms.ModelForm):
    class Meta:
        model = Leeds
        fields = ('status', 'comment', 'author')