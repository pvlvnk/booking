import datetime as dt


def year(request):
    current_date = dt.datetime.now()
    current_year = current_date.year
    return {
        'year': current_year
    }
