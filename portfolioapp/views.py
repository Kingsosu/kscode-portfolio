from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Construct the email message
        email_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\n\n{message}"

        try:
            send_mail(
                subject=subject,
                message=email_message,
                from_email=None,
                recipient_list=['kingsosuolale@gmail.com'], 
                fail_silently=False,
            )
            return JsonResponse({'success':True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})