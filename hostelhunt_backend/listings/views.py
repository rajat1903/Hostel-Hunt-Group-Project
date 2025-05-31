from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import HostelListing

# ======================
# API Views
# ======================

@csrf_exempt
@require_http_methods(["POST"])
def create_listing(request):
    """
    Create a new hostel listing
    
    Expected POST data:
    - roomType: Type of room (single/double/triple)
    - owner_name: Name of the hostel owner
    - location: Location of the hostel
    - rent: Monthly rent amount
    - contact: Contact number
    - description: Detailed description
    - image: Hostel image file
    
    Returns:
    - Success: JSON with status and listing ID
    - Error: JSON with error message
    """
    try:
        # Create new listing from form data
        listing = HostelListing.objects.create(
            room_type=request.POST.get('roomType'),
            owner_name=request.POST.get('owner_name'),
            location=request.POST.get('location'),
            monthly_rent=request.POST.get('rent'),
            contact=request.POST.get('contact'),
            description=request.POST.get('description'),
            image=request.FILES.get('image')
        )
        
        return JsonResponse({
            'status': 'success',
            'message': 'Listing created successfully',
            'id': listing.id
        })
    except Exception as e:
        print(f"Error creating listing: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

@require_http_methods(["GET"])
def get_listings(request):
    """
    Get all hostel listings
    
    Returns:
    - Success: JSON with list of listings
    - Error: JSON with error message
    
    Each listing includes:
    - id: Listing ID
    - room_type: Type of room
    - owner_name: Owner's name
    - location: Hostel location
    - monthly_rent: Monthly rent
    - contact: Contact number
    - description: Detailed description
    - image_url: URL of the hostel image
    - created_at: Creation timestamp
    """
    try:
        # Get all listings, newest first
        listings = HostelListing.objects.all().order_by('-created_at')
        listings_data = []
        
        # Convert each listing to dictionary
        for listing in listings:
            listings_data.append({
                'id': listing.id,
                'room_type': listing.room_type,
                'owner_name': listing.owner_name,
                'location': listing.location,
                'monthly_rent': float(listing.monthly_rent),
                'contact': listing.contact,
                'description': listing.description,
                'image_url': request.build_absolute_uri(listing.image.url) if listing.image else None,
                'created_at': listing.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        
        return JsonResponse({
            'status': 'success',
            'listings': listings_data
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400) 