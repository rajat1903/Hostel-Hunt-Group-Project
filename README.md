# HostelHunt

HostelHunt is a web application designed to help students find and book hostels easily. The platform provides a user-friendly interface for browsing hostel listings, viewing details, and managing bookings.

## Features
 
- Browse hostel listings with detailed information
- View hostel images and amenities
- Search and filter hostels based on preferences
- Add new hostel listings
- Responsive design for both desktop and mobile devices

## Tech Stack 

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap (for responsive design)

### Backend
- Django 5.0.2
- Flask 2.0.1
- Python

### Dependencies
- django-cors-headers
- flask-cors
- Pillow (for image handling)
- Werkzeug

## Project Structure

```
HostelHunt/
├── hostelhunt_backend/     # Django backend application
│   ├── listings/          # Hostel listings app
│   ├── media/            # Hostel images
│   └── manage.py         # Django management script
├── index.html            # Landing page
├── listings.html         # Hostel listings page
├── add-listing.html      # Add new hostel page
├── styles.css           # Main stylesheet
└── script.js            # Frontend JavaScript
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/rajat1903/Hostel-Hunt.git
cd Hostel-Hunt
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
cd hostelhunt_backend
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributors

1. Ankit Songara (Team Leader)
2. Shivam Kushwah (Developer)
3. Rajat Deshmukh (Developer)
4. Bulbul (Developer)
   
## Contact

Rajat Deshmukh - [@rajat1903](https://github.com/rajat1903)

Project Link: [https://github.com/rajat1903/Hostel-Hunt](https://github.com/rajat1903/Hostel-Hunt) 
