from django import forms


class FibonacciForm(forms.Form):
    name = forms.IntegerField()
    # message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
