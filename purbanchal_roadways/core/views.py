from django.shortcuts import render
from purbanchal_roadways.services.models import Service, Testimonial
from purbanchal_roadways.contact.models import Branch

def home(request):
    featured_services = Service.objects.filter(is_featured=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    main_office = Branch.objects.filter(is_main_office=True).first()

    context = {
        'featured_services': featured_services,
        'testimonials': testimonials,
        'main_office': main_office,
    }

    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def pricing(request):
    return render(request, 'core/pricing.html')

def faq(request):
    return render(request, 'core/faq.html')

def privacy_policy(request):
    return render(request, 'core/privacy.html')

def terms_of_service(request):
    return render(request, 'core/terms.html')

def write_review(request, category=None):
    context = {
        'category': category
    }
    return render(request, 'core/write_review.html', context)

def custom_quote(request):
    if request.method == 'POST':
        # Here you would process the form data
        # For now, we'll just render the template with a success message
        return render(request, 'core/custom_quote.html', {'success': True})
    return render(request, 'core/custom_quote.html')

def payment(request):
    if request.method == 'POST':
        # Here you would process the payment verification form
        # For now, we'll just render the template with a success message
        return render(request, 'core/payment.html', {'success': True})
    return render(request, 'core/payment.html')

def learn_more(request):
    return render(request, 'core/learn_more.html')
