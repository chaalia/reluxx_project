from django import forms

from blog.models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'user', 'category')
        # widgets = forms = {
        #     'category': forms.Select(choices=Post.CATEGORY_CHOICES),
        # }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
