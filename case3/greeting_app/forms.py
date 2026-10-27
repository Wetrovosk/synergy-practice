from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваше имя...',
                'autocomplete': 'off',
            })
        }
        error_messages = {
            'name': {
                'required': 'Пожалуйста, введите ваше имя.',
                'max_length': 'Имя не должно превышать 100 символов.'
            }
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('Имя не может состоять только из пробелов.')
        return name