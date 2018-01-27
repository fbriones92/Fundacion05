from django.shortcuts import render
from django.http.response import HttpResponse
from _datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def website(request):
    return render(request, 'app/banner.html', {
        'year':datetime.now().year,
    })
