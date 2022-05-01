from django.forms import ModelForm

from app.models import Comment


class RequestForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('__all__')
