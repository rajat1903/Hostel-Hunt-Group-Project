from django.db import models

class HostelListing(models.Model):
    """
    Model to store hostel listing information
    Fields:
    - room_type: Type of room (single/double/triple)
    - owner_name: Name of the hostel owner
    - location: Location of the hostel
    - monthly_rent: Monthly rent amount
    - contact: Contact number
    - description: Detailed description
    - image: Hostel image
    - created_at: Timestamp of when the listing was created 
    """
    
    # Room type choices
    ROOM_TYPES = [
        ('single', 'Single Room'),
        ('double', 'Double Sharing'),
        ('triple', 'Triple Sharing'),
    ]

    # Basic Information
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    owner_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    
    # Financial Information
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Contact Information
    contact = models.CharField(max_length=15)
    
    # Additional Details
    description = models.TextField()
    image = models.ImageField(upload_to='hostel_images/')
    
    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the hostel listing"""
        return f"{self.owner_name}'s {self.room_type} at {self.location}" 
