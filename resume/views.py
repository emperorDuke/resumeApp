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
    {"name": "VueJs", "progress": "99"},
    {"name": "ReactJs", "progress": "99"}
]

services = [
    {
        'title': 'Web Development',
        'body': 'I develop world class website for any client with HTML, CSS and JavaScript using any server side technology.'
    },
    {
        'title': 'SEO optimization ',
        'body': 'I carry search engine optimizations for any clients that requires a high ranking with search engines like google, bing etc.'
    },
]

educations = [
    {
        'year': '2016-2021',
        'degree': 'Master degree - Ahmadu Bello University, Zaria',
        'course': 'Industrial Microbiology',
    },
    {
        'year': '2011-2015',
        'degree': 'Bsc degree - University of Ilorin, Ilorin',
        'course': 'Microbiology',
    }
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
            'services': services,
            'educations': educations,
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
                'status': 'danger',
            }
        )

        return render(
            request,
            "resume/status.html",
            context,
        )
