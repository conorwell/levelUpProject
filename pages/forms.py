from django import forms
class summarize(forms.Form):
    Text = forms.CharField(required=True)
