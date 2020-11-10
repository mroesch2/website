from django.shortcuts import render
from django.http import HttpResponse    #Added for Contact Form
from .forms import ContactForm          #Added for Contact Form
from django.core.mail import send_mail  #Added for Contact Form

# Create your views here.
def homepage(request):
    return render(request, "website/homepage.html", {
       
    })


def resume(request):
    return render(request, "website/resume.html", {

    })

#Code pulled from https://diagramy.com/blog/2018/05/17/django-contact-us-tutorial/
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['mroesch2@gmail.com'])
            return HttpResponse('Thanks for your message!')
    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form': form})