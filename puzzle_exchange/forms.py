from django import forms
from .widgets import CustomClearableFileInput
from .models import PuzzleExchange

class PuzzleExchangeForm(forms.ModelForm):

  class Meta:
    model = PuzzleExchange
    fields = ['title', 'body', 'image']

image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    for field_name, field in self.fields.items():
      field.widget.attrs['class'] = 'border-dark rounded'



