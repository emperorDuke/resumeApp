from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, help_text='i would like to know you')
    email = forms.EmailField(help_text='i would like to get back to you', required=True)
    message = forms.CharField(help_text='How can i be of service', required=True, max_length=1000, widget=forms.Textarea)