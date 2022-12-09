from django import forms

class dataBaseForm(forms.Form):
    # server = forms.CharField(initial="whatever you want")
    # database = forms.CharField()
    # username = forms.CharField()
    # password = forms.CharField()
    # driver= forms.CharField()

    SERVER_CHOICES = {
        (1, 'Triumph'),
        (2, 'TAF'),
        (3, 'Karl')
    }

    server = forms.ChoiceField(choices=SERVER_CHOICES)
    source = forms.CharField()
    key_columns = forms.CharField()
    columns = forms.CharField()