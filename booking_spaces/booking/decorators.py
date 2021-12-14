from django.shortcuts import redirect


def manager_or_admin_only(func):
    def check_user(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role in ['manager', 'admin']:
            return func(request, *args, **kwargs)
        return redirect('booking:index')
    return check_user
