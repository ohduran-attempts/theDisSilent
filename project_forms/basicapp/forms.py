from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                                                widget=forms.HiddenInput)  # input of type hidden

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        # a human won't ever fill this value
        if len(botcatcher) > 0:
            raise forms.ValidationError("Gotcha, bot!")
        return botcatcher
