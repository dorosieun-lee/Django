from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'
        labels = {
            "location": "Location",
            "plan": "Plan",
            "start_date": "Start Date",
            "end_date": "End Date"
        }
        widgets = {
            "location": forms.TextInput(attrs={
                'placeholder':"ex) 제주도"}),
            "plan": forms.Textarea(attrs={
                'rows': 5,
                'cols': 40,
                'placeholder' : "ex) 슉.슈슉."}),
            "start_date": forms.DateInput(attrs={
                'placeholder': "ex) 2022-02-22"
            }),
            "end_date": forms.DateInput(attrs={
                'placeholder': "ex) 2022-02-22"
            })
        }