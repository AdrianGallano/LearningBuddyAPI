from tinymce.widgets import TinyMCE
from django.forms import ModelForm
from .models import Topic

class EditorForm(ModelForm):

    class Meta:
        model = Topic
        fields = ["content"]
        widgets = {'content': TinyMCE()}
