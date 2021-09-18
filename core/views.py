from django.shortcuts import render


def home(request):
    context = {
        'title': 'Md Joy Islam'
    }
    return render(request, 'social_media.html', context)
