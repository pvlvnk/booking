from django import forms
from booking.models import Schedule
from datetime import datetime as dt


class ReservingForm(forms.ModelForm):
    reserving_dates = forms.ModelMultipleChoiceField(
        queryset=Schedule.objects.filter(
            is_reserved=False).filter(reserving_date__gte=dt.today()),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Schedule
        fields = ('reserving_dates',)


class EditReservingForm(forms.ModelForm):
    reserving_dates = forms.ModelMultipleChoiceField(
        queryset=Schedule.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Schedule
        fields = ('reserving_dates',)


class CreationSchedule(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('space', 'reserving_date',)


class DeletionSchedule(forms.ModelForm):
    reserving_dates = forms.ModelMultipleChoiceField(
        queryset=Schedule.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Schedule
        fields = ('reserving_dates',)
