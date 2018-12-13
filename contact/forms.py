from django import forms

class contactForm(forms.Form):
    name = forms.CharField(help_text='100 characters max.', max_length=100, required=False)
    email = forms.EmailField(required = True)
    comment  = forms.CharField(required=True,widget=forms.Textarea) 