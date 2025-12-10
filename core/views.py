from django.shortcuts import render
from .models import Contact,Project  # Model import karein
from django.contrib import messages


def home(request):
    # Database se saare projects laayein
    projects = Project.objects.all().order_by('-created_at') # Newest pehle
    
    context = {
        'projects': projects
    }
    return render(request, 'core/home.html', context)


# core/views.py mein add karein

def about(request):
    return render(request, 'core/about.html')



# Contact View Logic
def contact(request):
    if request.method == "POST":
        # HTML form se data nikaalo
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Database mein save karo
        contact_entry = Contact(name=name, email=email, subject=subject, message=message)
        contact_entry.save()

        # Success message show karo
        messages.success(request, 'Your message has been sent successfully!')
        
    return render(request, 'core/contact.html')




# NEW VIEW FOR PROJECTS
def projects_page(request):
    # Saare projects yahan load honge
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'core/projects.html', {'projects': projects})




# ... purane imports ...

def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)

def custom_500(request):
    return render(request, 'core/500.html', status=500)




def privacy_policy(request):
    return render(request, 'core/privacy.html')

def terms_of_service(request):
    return render(request, 'core/terms.html')