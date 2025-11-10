from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'post_date', 'location', 'is_public', 'allow_comments', 'allow_sharing', 'mood', 'tag_people', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Title of your post'}),
            'description': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Write something...', 'rows':4}),
            'post_date': forms.DateInput(attrs={'class': 'input-field', 'type':'date'}),
            'location': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Location'}),
            'mood': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Your mood'}),
            'tag_people': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Tag people, comma-separated'}),
        }
