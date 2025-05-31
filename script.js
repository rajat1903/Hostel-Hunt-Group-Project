// ======================
// Navigation Functions
// ======================

/**
 * Initialize navigation functionality
 * - Handles active state of navigation links
 * - Sets up explore button click handler
 */
function initializeNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    const exploreBtn = document.querySelector('.explore-btn');

    // Handle navigation link clicks
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            // Add active class to clicked link
            e.currentTarget.classList.add('active');
        });
    });

    // Handle explore button click
    if (exploreBtn) {
        exploreBtn.addEventListener('click', () => {
            window.location.href = 'listings.html';
        });
    }
}

// ======================
// Form Submission Functions
// ======================

/**
 * Handle hostel listing form submission
 * - Collects form data
 * - Sends to backend
 * - Handles success/error responses
 */
async function handleListingSubmit(e) {
    e.preventDefault();
    
    try {
        // Get form data
        const formData = new FormData(e.target);
        
        // Send to backend
        const response = await fetch('http://localhost:8000/api/listings/create/', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        
        if (response.ok) {
            alert('Listing created successfully!');
            window.location.href = 'listings.html';
        } else {
            alert('Error: ' + data.message);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error submitting form: ' + error.message);
    }
}

// ======================
// Page Initialization
// ======================

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize navigation
    initializeNavigation();
    
    // Set up form submission if on add-listing page
    const listingForm = document.querySelector('.listing-form');
    if (listingForm) {
        listingForm.addEventListener('submit', handleListingSubmit);
    }
}); 