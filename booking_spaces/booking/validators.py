from django.core.exceptions import ValidationError
from datetime import datetime as dt

def date_validator(value):
    if value < dt.today().date():
        raise ValidationError(
            'Нельзя указывать прошедшую дату'
        )
