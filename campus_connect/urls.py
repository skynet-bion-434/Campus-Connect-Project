from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# Temporary views to render templates directly (you can replace with real views later)
def home(request):
    return render(request, "base.html", {"title": "Home"})

def about(request):
    return render(request, "about.html", {"title": "About"})

def contact(request):
    return render(request, "contact.html", {"title": "Contact"})

def privacy(request):
    return render(request, "privacy.html", {"title": "Privacy Policy"})

def terms(request):
    return render(request, "terms.html", {"title": "Terms of Service"})

def dashboard(request):
    return render(request, "dashboard.html", {"title": "Dashboard"})

def profile(request):
    return render(request, "profile.html", {"title": "Profile"})

urlpatterns = [
    path("admin/", admin.site.urls),

    # Public routes
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("privacy/", privacy, name="privacy"),
    path("terms/", terms, name="terms"),

    # Auth-related routes (placeholders, you can connect to Django auth later)
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/", profile, name="profile"),
]
