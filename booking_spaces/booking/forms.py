from booking.models import Schedule, ParkingSpace
from datetime import datetime as dt

from django import forms



class ReservingForm(forms.ModelForm):
    reserving_dates = forms.ModelMultipleChoiceField(
        queryset=Schedule.objects.filter(reserving_date__gte=dt.today()),
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


class CreationScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('space', 'reserving_date',)


class DeletionScheduleForm(forms.ModelForm):
    deleting_dates = forms.ModelMultipleChoiceField(
        queryset=Schedule.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Schedule
        fields = ('deleting_dates',)


class CreationSpaceForm(forms.ModelForm):
    class Meta:
        model = ParkingSpace
        fields = ('title', 'slug', 'image')


class DeletionSpaceForm(forms.ModelForm):
    deleting_spaces = forms.ModelMultipleChoiceField(
        queryset=ParkingSpace.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
    class Meta:
        model = ParkingSpace
        fields = ('deleting_spaces',)