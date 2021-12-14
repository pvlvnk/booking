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

    def validate_date(self, request):
        data = self.cleaned_data['reserving_dates']
        reserved_dates = Schedule.objects.filter(space=request.space)
        for reserving_date in data:
            for reserved_date in reserved_dates:
                if reserving_date == reserved_date.reserving_date:
                    raise forms.ValidationError('Дата уже занята')
        return data


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
