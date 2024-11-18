from django import forms

from blogs.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('author',)
        # fields = ('title', 'about', 'published_date')
