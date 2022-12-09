from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class tableBaseForm(forms.Form):
    # server = forms.CharField(initial="whatever you want")
    # database = forms.CharField()
    # username = forms.CharField()
    # password = forms.CharField()
    # driver= forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse('process')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    SERVER_CHOICES = {
        (1, 'Triumph'),
        (2, 'TAF'),
        (3, 'Karl')
    }

    server = forms.ChoiceField(choices=SERVER_CHOICES)
    source = forms.CharField()
    key_columns = forms.CharField()
    columns = forms.CharField()
