from django import forms

from instagram.models import Posts


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('description', 'img')

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if len(description) < 3:
            raise forms.ValidationError('Количество символов должно быть больше 2 символов')



