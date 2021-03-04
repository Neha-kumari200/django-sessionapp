from django.shortcuts import render

# Create your views here.


def setsession(request):
    request.session['name'] = 'Neha'
    request.session['lname'] = 'Singh'
    return render(request, 'testapp/setsession.html')


def getsession(request):
    name = request.session.get('name', default="None")
    lname = request.session.get('lname', default="None")
    #name = request.session('name')
    return render(request, 'testapp/getsession.html', {'name': name, 'lname': lname})


def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'testapp/delsession.html')


