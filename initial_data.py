import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'purbanchal_roadways_main.settings')
django.setup()

from services.models import Service, Testimonial
from contact.models import Branch

# Create services
services = [
    {
        'title': 'Household Goods Transport',
        'description': 'Safe & secure household goods transport with 100% care for your valuable items. We understand that your household items are not just possessions but memories and emotions. Our specialized household goods transport service ensures that your belongings are handled with the utmost care and delivered safely to your new home.',
        'icon': 'fas fa-home',
        'is_featured': True
    },
    {
        'title': 'Car Transport Services',
        'description': 'Fast, reliable car booking and delivery from your doorstep to any city in India. Moving to a new city and want to take your car along? Our car transport service provides a safe and reliable solution for transporting your vehicle across India. We use specialized car carriers to ensure your vehicle reaches its destination in the same condition as it was picked up.',
        'icon': 'fas fa-car',
        'is_featured': True
    },
    {
        'title': 'Door-to-Door Delivery',
        'description': 'Hassle-free pickup and drop at your convenience, anywhere in India. Our door-to-door delivery service eliminates the hassle of transporting your goods to and from our facilities. We pick up your items from your current location and deliver them directly to your specified destination, providing a seamless and convenient experience.',
        'icon': 'fas fa-truck',
        'is_featured': True
    },
    {
        'title': 'Packing Facility',
        'description': 'Professional packing services to ensure your items are protected during transit. Proper packing is essential for the safe transportation of your goods. Our professional packing service uses high-quality materials and techniques to ensure that your items are protected during transit. We offer customized packing solutions based on the nature and fragility of your items.',
        'icon': 'fas fa-box',
        'is_featured': True
    },
    {
        'title': 'Insurance Facility',
        'description': 'Comprehensive insurance coverage for your valuable goods during transportation. We offer comprehensive insurance coverage for your goods during transportation, giving you peace of mind. Our insurance facility covers damages, losses, or theft during transit, ensuring that your valuable possessions are protected against unforeseen circumstances.',
        'icon': 'fas fa-shield-alt',
        'is_featured': False
    },
    {
        'title': 'Tracking Facility',
        'description': 'Real-time tracking of your shipments to know exactly where your goods are. Stay informed about the location and status of your shipment with our real-time tracking facility. Our advanced tracking system allows you to monitor the movement of your goods throughout the transportation process, providing transparency and peace of mind.',
        'icon': 'fas fa-map-marker-alt',
        'is_featured': False
    }
]

for service_data in services:
    Service.objects.create(**service_data)

# Create testimonials
testimonials = [
    {
        'name': 'Rajesh Kumar',
        'position': 'Dibrugarh',
        'content': 'I recently used Purbanchal Roadways for shifting my household goods from Dibrugarh to Delhi. The service was excellent, and all my items reached safely without any damage. Highly recommended!',
        'is_active': True
    },
    {
        'name': 'Priya Sharma',
        'position': 'Sivasagar',
        'content': 'Purbanchal Roadways provided exceptional service when I needed to transport my car from Sivasagar to Mumbai. The team was professional, and the delivery was on time. Great experience!',
        'is_active': True
    },
    {
        'name': 'Amit Singh',
        'position': 'Guwahati',
        'content': 'I have been using Purbanchal Roadways for my business logistics needs for the past 5 years. Their reliability and efficiency have made them my go-to transport partner. Excellent service!',
        'is_active': True
    }
]

for testimonial_data in testimonials:
    Testimonial.objects.create(**testimonial_data)

# Create branches
branches = [
    {
        'name': 'Dibrugarh Head Office',
        'address': 'G-1, Mannat Villa, Park Street, M.R. Road, Naliapool, Dibrugarh-786001, Assam, India',
        'phone': '+91 9435055251 / +91 7002269499',
        'email': 'purbanchal.1997@gmail.com',
        'is_main_office': True
    },
    {
        'name': 'Sivasagar Branch Office',
        'address': 'Ward No.-12, Near SBI ATM, Jamuna Road, P.O. & Distt. Sivasagar, Assam, India, PIN-785640',
        'phone': '+91 9435055251 / +91 7002269499',
        'email': 'purbanchal.1997@gmail.com',
        'is_main_office': False
    }
]

for branch_data in branches:
    Branch.objects.create(**branch_data)

print("Initial data loaded successfully!")
