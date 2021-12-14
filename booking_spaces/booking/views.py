from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView

from booking.forms import EditReservingForm, ReservingForm, CreationSchedule
from booking.models import ParkingSpace, Schedule
from booking.decorators import manager_or_admin_only


def index(request):
    spaces = ParkingSpace.objects.all()
    user = request.user
    context = {
        'spaces': spaces,
        'user': user
    }
    return render(request, 'booking/index.html', context)


@login_required
def space_reserving(request, slug):
    form = ReservingForm()
    context = {
        'form': form,
        'space': get_object_or_404(ParkingSpace, slug=slug),
    }
    if request.method != 'POST':
        return render(request, 'booking/reserving.html', context)
    form = ReservingForm(
        request.POST or None,
        files=request.FILES or None
    )
    if not form.is_valid():
        return render(request, 'booking/reserving.html', context)
    objects = form.cleaned_data['reserving_dates'].values()
    for object in objects:
        reserving_date = get_object_or_404(Schedule, id=object['id'])
        reserving_date.is_reserved = True
        reserving_date.booking_user = request.user
        reserving_date.save(update_fields=['is_reserved', 'booking_user'])
    return redirect('booking:index')


@login_required
def reserve_edit(request, slug, username):
    form = EditReservingForm()
    form.fields['reserving_dates'].queryset = Schedule.objects.filter(
        booking_user=request.user)
    context = {
        'form': form,
        'is_edit': True,
        'space': get_object_or_404(ParkingSpace, slug=slug)
    }
    if request.method != 'POST':
        return render(request, 'booking/reserving.html', context)
    form = EditReservingForm(
        request.POST or None,
        files=request.FILES or None,
    )
    form.fields['reserving_dates'].queryset = Schedule.objects.filter(
        booking_user=request.user
    )
    if form.is_valid():
        objects = form.cleaned_data['reserving_dates'].values()
        for object in objects:
            reserving_date = get_object_or_404(Schedule, id=object['id'])
            reserving_date.is_reserved = False
            reserving_date.booking_user = None
            reserving_date.save(update_fields=['is_reserved', 'booking_user'])
    return render(request, 'booking/reserving.html', context)


@manager_or_admin_only
def CreateSchedule(request):
    form = CreationSchedule()
    context = {
        'form': form,
    }
    if request.method != 'POST':
        return render(request, 'booking/create_schedule.html', context)
    form = ReservingForm(
        request.POST or None,
        files=request.FILES or None
    )
    if not form.is_valid():
        return render(request, 'booking/create_schedule.html', context)
    form.save()
    return render(request, 'booking/create_schedule.html', context)




class InfoView(TemplateView):
    template_name = 'booking/info.html'
