from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import ContactForm

def index(request):
    template = 'index.html'
    name = ''

    contact_form = ContactForm(request.POST or None)

    python_queryset = ['Django REST Framework', 'Knowledgable with Python STD library', 'Custom Authentication/Authorization', '3rd party libraries e.g Virtualenv, Virtualenvwrapper, crispy_forms, django-registration-redux etc.',]

    ui_queryset = ['HTML5/CSS3 ', 'Bootstrap 3+', 'Javascript and libraries e.g AngularJS and Jquery', 'Font-icons and 3rd party iconic fonts e.g FontAwesome', '2-Way data binding and loose coupling with AngularJS']

    osx_queryset = ['Intermediate knowledge of Ubuntu Linux/BASH', 'SSH VirtualBox and Vagrant', 'Postgresql/MySQL/sqlite3', 'Version control with Git', 'VIM!']

    if request.user.is_authenticated():
        current_user = request.user.get_full_name()
        name,domain = current_user.split('@')

    context = {
        'username': name,
        'py_query': python_queryset,
        'ui_query': ui_queryset,
        'osx_query': osx_queryset,
        'contact_form': contact_form
    }

    if contact_form.is_valid():
        form_name = contact_form.cleaned_data.get('name')
        form_email = contact_form.cleaned_data.get('email')
        form_message = contact_form.cleaned_data.get('message')

        subject = "Jcain Portfolio Contact"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]

        contact_message = "%s: %s via %s"%(
            form_name,
            form_message,
            form_email
        )

        send_mail(subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=False)

        del context['contact_form']
        context['confirm_message'] = 'Thank you for contacting us!'



    return render(request, template, context)
