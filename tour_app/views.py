from django.http import HttpResponse
from django.shortcuts import render

from tour_app.models import Division, Location, GuideDetails, Thana


def index(request):
    division = Division.objects.all()
    context = {
        'division': division
    }
    return render(request, 'index.html', context)

def location(request):
    # query parameter
    division = request.GET.get('division', '')
    if division=='':
        location = Location.objects.all()
    else:
        location = Location.objects.filter(division=division)

    context = {
        'location': location
    }
    return render(request, 'location.html', context)

def location_detail(request, pk):
    location = Location.objects.get(pk=pk)
    thana = Thana.objects.all()
    context = {
        'location': location,
        'thana' : thana
    }
    return render(request, 'location_details.html', context)

def blog(request):
    return render(request, 'blog.html')

def image(request):
    img= Location.objects.all()
    context={
        'img': img
    }
    return render(request, 'image.html', context)

def tour_guide(request):
    tour_guide = GuideDetails.objects.all()
    context = {
        'tour_guide' : tour_guide
    }
    return render(request, 'tour_guide.html', context)

