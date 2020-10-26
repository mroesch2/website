from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "website/homepage.html", {
       
    })

def aboutme(request):
    return render(request, "website/aboutme.html", {

    })

def resume(request):
    return render(request, "website/resume.html", {

    })