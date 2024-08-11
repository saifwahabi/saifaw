from django.shortcuts import render, get_object_or_404
from .models import Project, Mockup, Contact, Site_data
from .forms import ContactForm


data = Site_data.objects.first()

# Create your views here.
def home(request):
    context = {
        "page": "home",
        "projects": Project.objects.filter(visible_home=True),
        "project_number": len(Project.objects.filter(visible_work=True)),
        "data":data
    }
    return render(request, "home.html", context)

def about(request):
    context = {
        "page": "about",
        "data":data
    }
    return render(request, "about.html", context)

def work(request):
    context = {
        "page": "work",
        "projects": Project.objects.filter(visible_work=True),
        "development_number": len(Project.objects.filter(visible_work=True, development=True)),
        "design_number": len(Project.objects.filter(visible_work=True, design=True)),
        "data":data
    }
    return render(request, "work.html", context)

def contact(request):
    context = {
        "page": "contact",
        "data":data
    }


    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Seccussesful")
            return render(request, "success.html", {"page": "success"})
        else :
            print(form.errors)

    return render(request, "contact.html", context)




def project(request, pk):    
    project = get_object_or_404(Project, name=pk) 
    mockups = Mockup.objects.filter(project=project.id).order_by('order')
    all_projects = Project.objects.order_by('id')
    current_project_index = list(all_projects.values_list('id', flat=True)).index(project.id)

    if current_project_index == len(all_projects) - 1:
        next_project = all_projects.first()  # Wrap around to the first project
    else:
        next_project = all_projects[current_project_index + 1]

    context = {
        "project": pk,
        "project_data": project,
        "project_number": len(Project.objects.filter(visible_work=True)),
        "page": pk,
        "mockups": mockups,
        "main_background_color": Mockup.objects.filter(project=project.id).latest("order").background_color,
        "next_project": next_project,
        "data": data
    }
    return render(request, "project.html", context)


def contact_success(request):
    context={
        "page": "success",
        "data": data
    }
    return render(request, "success.html", context)

def error_404(request, exception):
    context={
        "page": "error",
        "data": data
    }
    return render(request, '404.html', context, status=404)