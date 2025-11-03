from django.shortcuts import redirect

def dangxuat_view(request):
    request.session.flush()
    return redirect('homePage')
