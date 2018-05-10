# -*- coding: utf-8 -*-
from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000, help_text="maximalne 4000 znaku")

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']
