from django.conf import settings
from booking.decorators import manager_or_admin_only
from booking.forms import (CreationScheduleForm, DeletionScheduleForm,
                           EditReservingForm, ReservingForm, CreationSpaceForm, DeletionSpaceForm)
from booking.models import ParkingSpace, Schedule
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView
from django.views.decorators.cache import cache_page

@cache_page(20, key_prefix='index_page')
def index(request):
    spaces = ParkingSpace.objects.all()
    paginator = Paginator(spaces, settings.AMOUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    user = request.user
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'booking/index.html', context)


@login_required
def space_reserving(request, slug):
    current_space = get_object_or_404(ParkingSpace, slug=slug)
    form = ReservingForm()
    form.fields['reserving_dates'].queryset = Schedule.objects.filter(
        space=current_space, is_reserved=False)
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
    current_space = get_object_or_404(ParkingSpace, slug=slug)
    form = EditReservingForm()
    form.fields['reserving_dates'].queryset = Schedule.objects.filter(
        space=current_space).filter(booking_user=request.user)
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
    return redirect('booking:index')


@manager_or_admin_only
def CreateSchedule(request):
    form = CreationScheduleForm()
    context = {
        'form': form,
        'create_schedule': True,
    }
    if request.method != 'POST':
        return render(request, 'booking/create_schedule.html', context)
    form = CreationScheduleForm(
        request.POST or None,
        files=request.FILES or None
    )
    if not form.is_valid():
        return render(request, 'booking/index.html', context)
    form.save()
    context = {
        'form': form,
        'create_schedule': True,
        'alert_flag': True,
    }
    return render(request, 'booking/create_schedule.html', context)


@manager_or_admin_only
def DeleteSchedule(request):
    form = DeletionScheduleForm()
    context = {
        'form': form,
        'delete_schedule': True,
    }
    if request.method != 'POST':
        return render(request, 'booking/delete_schedule.html', context)
    form = DeletionScheduleForm(
        request.POST or None,
        files=request.FILES or None
    )
    if not form.is_valid():
        return render(request, 'booking/delete_schedule.html', context)
    objects = form.cleaned_data['deleting_dates'].values()
    for object in objects:
        reserving_date = get_object_or_404(Schedule, id=object['id'])
        reserving_date.delete()
    context = {
        'form': form,
        'delete_schedule': True,
        'alert_flag': True,
    }
    return render(request, 'booking/delete_schedule.html', context)


@manager_or_admin_only
def CreateSpace(request):
    form = CreationSpaceForm()
    context = {
        'form': form,
        'create_space': True,
    }
    if request.method != 'POST':
        return render(request, 'booking/create_space.html', context)
    form = CreationSpaceForm(
        request.POST or None,
        files=request.FILES or None
    )
    if not form.is_valid():
        return render(request, 'booking/index.html', context)
    form.save()
    context = {
        'form': form,
        'create_space': True,
        'alert_flag': True,
    }
    return render(request, 'booking/create_space.html', context)


@manager_or_admin_only
def DeleteSpace(request):
    form = DeletionSpaceForm()
    context = {
        'form': form,
        'delete_space': True,
    }
    if request.method != 'POST':
        return render(request, 'booking/delete_space.html', context)
    form = DeletionSpaceForm(
        request.POST or None,
        files=request.FILES or None
    )
    if not form.is_valid():
        return render(request, 'booking/delete_space.html', context)
    objects = form.cleaned_data['deleting_spaces'].values()
    for object in objects:
        reserving_date = get_object_or_404(ParkingSpace, id=object['id'])
        reserving_date.delete()
    context = {
        'form': form,
        'delete_schedule': True,
        'alert_flag': True,
    }
    return render(request, 'booking/delete_space.html', context)


class InfoView(TemplateView):
    template_name = 'booking/info.html'
