from django import forms
from counter.models import Subscriber



class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = '__all__'
