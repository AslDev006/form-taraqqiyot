from django import forms
from .models import Leeds
from phonenumber_field.formfields import PhoneNumberField



class LeedsForm(forms.ModelForm):
    phonenumber = forms.IntegerField(min_value=0, max_value=999999999)
    class Meta:
        model = Leeds
        fields = "__all__"


class LeedsFormUpdateForm(forms.ModelForm):
    class Meta:
        model = Leeds
        fields = ('status', 'comment', 'author')