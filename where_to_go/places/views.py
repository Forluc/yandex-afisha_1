from django.shortcuts import render


def places(request):
    context = {}
    return render(request, 'index.html', context=context)
