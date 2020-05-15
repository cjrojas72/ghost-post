from django import forms
from posts.models import Post


class AddPostForm(forms.Form):
    CHOICE = (
        (True, 'boasts'),
        (False, 'roasts')
    )
    name = forms.CharField(max_length=50, required=True)
    choice = forms.ChoiceField(choices=CHOICE, label="Roast or Boast",
                               initial='', widget=forms.Select(), required=True)
    user_input = forms.CharField(widget=forms.Textarea, required=True)
