from django import forms
from .models import Tag, Topic
from django.core.exceptions import ValidationError


class MLGForm(forms.Form):
    word1 = forms.CharField()
    word2 = forms.IntegerField(required=False)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cats'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cats'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('slug can\'t be "create"')
        return new_slug


class TopicForm(forms.ModelForm):

    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = Topic
        fields = ['blog', 'title', 'body', 'author', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cats'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'cats'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def save(self, *args, **kwargs):
        new_topic = super().save(*args, **kwargs)
        for tag in self.cleaned_data['tags']:
            new_topic.tags.add(tag)
        return new_topic
