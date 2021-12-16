from booking.validators import date_validator
from django.db import models
from django.db.models import constraints
from users.models import User


class ParkingSpace(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='title'
        )
    slug = models.SlugField(
        unique=True,
        verbose_name='slug'
    )
    image = models.ImageField(
        'Image',
        upload_to='spaces/',
        blank=True
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Space'
        verbose_name_plural = 'Spaces'

    def __str__(self):
        return self.title


class Schedule(models.Model):
    space = models.ForeignKey(
        ParkingSpace,
        on_delete=models.CASCADE,
        related_name='shedule',
        verbose_name='space',
        help_text='choose space'
    )
    reserving_date = models.DateField(
        validators=[date_validator],
        verbose_name='date',
        help_text='format %Y-%m-%d'
        )
    is_reserved = models.BooleanField(default=False)
    is_past = models.BooleanField(default=False)
    booking_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        constraints = (
            constraints.UniqueConstraint(
                fields=('space', 'reserving_date'), name='unique_reserve'),
        )


    def __str__(self):
        return f'{self.space.title} - {self.reserving_date}'
