from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
from profiles.models import UserProfile


def contact(request):
    """
    View to handle contact form submission and pre-fill fields for
    authenticated users
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request,
                'Your message was sent successfully. '
                'Please allow up to 2 working days for a response.'
            )
            return redirect('home')
        else:
            messages.error(
                request,
                'There was an error sending your message. '
                'Please ensure all fields are valid and try again.'
            )
            return redirect('contact')

    else:
        if request.user.is_authenticated:
            try:
                # form pre-filled with user's default information
                user = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'contact_email': user.user.email,
                    'contact_phone_number': user.default_phone_number,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': contact_form,
    }

    return render(request, template, context)
