from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactForm
from .models import Contact

# Create your views here.

contacts = [
    {"icon": "phone", "value": "+234703606116"},
    {"icon": "email", "value": "effiomduke@gmail.com"},
]

hobbies = [
    {"name": "writting", "icon": "pencil"},
    {"name": "football", "icon": "soccer"},
    {"name": "travelling", "icon": "airplane"},
    {"name": "gaming", "icon": "controller-classic"},
    {"name": "movies", "icon": "movie"},
]

skills = [
    {"name": "Python", "progress": "85"},
    {"name": "PHP", "progress": "80"},
    {"name": "Django", "progress": "90"},
    {"name": "Laravel", "progress": "95"},
    {"name": "Javascript", "progress": "99"},
]


def hompage(request):
    form = ContactForm()

    return render(
        request,
        "resume/index.html",
        {
            "form": form,
            "hobbies": hobbies,
            "contacts": contacts,
            "skills": skills,
            "profile": "To obtain a position that will enable me use my strong organizational skills, award-winning educational background, and ability to work well with people.",
        },
    )


def handle_form(request):
    context = {
        "hobbies": hobbies,
        "contacts": contacts,
    }
    # create a form instance and populate it with data from the request:
    if request.method == "POST":
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            contact = Contact.objects.create(**form.cleaned_data)

            if contact:
                context.update(
                    {
                        'icon': 'emoticon-outline',
                        'username': contact.name,
                        'status': 'success'
                    }
                )
                return render(
                    request,
                    "resume/status.html",
                    context,
                )

        context.update(
            {
                'icon': 'emoticon-sad-outline',
                'status': 'error',
            }
        )

        return render(
            request,
            "resume/status.html",
            context,
        )
