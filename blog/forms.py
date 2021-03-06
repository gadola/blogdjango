from .models import Comment,Post
from django import forms

class CommentForms(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author',None)
        self.post = kwargs.pop('post',None)
        super().__init__(*args, **kwargs)

    def save(self,commit = True):
        comment =super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()

    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body':forms.Textarea(attrs={'cols':'40','rows':'1',"class":"form-control"}),
        }


class PostForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        self.author = kwargs.pop('author', None)
        super().__init__(*args,**kwargs)

    def save(self,commit = True):
        post =super().save(commit=False)
        post.author = self.author
        post.save()

    class Meta:
        model = Post
        fields = ['title','text', 'image']
        widgets = {
            'text':forms.Textarea(attrs={'placeholder':"Content" ,'class':"form-control",}),
            'title':forms.TextInput(attrs={'placeholder':"Title" ,'class':"form-control"}),
        }

class PostUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','text', 'image']
        widgets = {
            'text':forms.Textarea(attrs={'placeholder':"Content" ,'class':"form-control",}),
            'title':forms.TextInput(attrs={'placeholder':"Title" ,'class':"form-control"}),
        }
        success_url ="/"

