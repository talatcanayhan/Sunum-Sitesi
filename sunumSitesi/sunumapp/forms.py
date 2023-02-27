from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ["isim", "yorum"]
    labels = {'isim': "name", "yorum": "comment"}
    