from django.shortcuts import render

def home(request):
    context = {
        "description": "Welcome to my creative world! Let’s build something amazing together."  # ✅ Dynamic text
    }
    return render(request, "portfolio/home.html", context)

def projects(request):
    return render(request, "portfolio/projects.html")

def about(request):  # ✅ Ensure this exists
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, "portfolio/contact.html")
def projects(request):
    return render(request, 'portfolio/projects.html')  # ✅ Make sure this path is correct