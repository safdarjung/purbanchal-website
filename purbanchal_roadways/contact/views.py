from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactInquiry, Branch
from .forms import ContactForm

def contact(request):
    branches = Branch.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your inquiry has been submitted successfully. We will contact you soon.')
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'branches': branches,
        'form': form
    }

    return render(request, 'contact/contact.html', context)
