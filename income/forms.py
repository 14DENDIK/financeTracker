from django import forms
import datetime
from django.db.models import Q
from .models import Income, IncomeType


class IncomeForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.fields['type'].queryset = IncomeType.objects.filter(Q(user=None) | Q(user=user))

    date = forms.DateField(
        initial=datetime.date.today,
        input_formats=['%Y/%m/%d'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2',
        })
    )
    amount = forms.DecimalField(
        max_digits=14,
        decimal_places=2,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Amount'
        })
    )
    type = forms.ModelChoiceField(
        initial=IncomeType.objects.get(name='salary'),
        queryset=IncomeType.objects.none(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'data-width': 'auto',
        })
    )

    class Meta:
        model = Income
        fields = [
            'amount',
            'date',
            'type',
        ]
