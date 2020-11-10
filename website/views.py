from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "website/homepage.html", {
       
    })

def contact(request):
    return render(request, "website/contact.html", {

    })

def resume(request):
    return render(request, "website/resume.html", {

    })