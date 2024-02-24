from django.shortcuts import render
from .models import ProjectDetails  # Importing the ProjectDetails model

def index(request):
    context = {}

    # Retrieving web projects if they exist
    if ProjectDetails.objects.filter(jobtype='web').exists():
        context['webprojects'] = ProjectDetails.objects.filter(jobtype='web')

    # Retrieving UI projects if they exist
    if ProjectDetails.objects.filter(jobtype='ui').exists():
        context['uiprojects'] = ProjectDetails.objects.filter(jobtype='ui')

    return render(request, 'index.html', context)
