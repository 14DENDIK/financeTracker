from django import forms
import datetime
from .models import Expanse, ExpanseType
from django.db.models import Q


class ExpanseForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ExpanseForm, self).__init__(*args, **kwargs)
        self.fields['type'].queryset = ExpanseType.objects.filter(Q(user=None) | Q(user=user))

    date = forms.DateField(
        initial=datetime.date.today,
        input_formats=['%Y/%m/%d'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1',
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
        initial=ExpanseType.objects.get(name='food'),
        queryset=ExpanseType.objects.none(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'data-width': 'auto',
        })
    )

    class Meta:
        model = Expanse
        fields = [
            'amount',
            'type',
            'date',
        ]
