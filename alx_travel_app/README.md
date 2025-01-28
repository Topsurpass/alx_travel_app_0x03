# ALX Travel App

The ALX Travel App is a Django-based application designed for listing, booking, and reviewing travel accommodations. This project demonstrates creating database models, serializers for API representation, and management commands for seeding the database with sample data.

## Features

-   **Listings**: Add, view, and manage listings for travel accommodations.
-   **Bookings**: Book accommodations and manage reservations.
-   **Reviews**: Leave ratings and comments for listings.

## Project Structure

```
alx_travel_app_0x00/
├── alx_travel_app/
│   ├── listings/
│   │   ├── models.py            # Contains the Listing, Booking, and Review models
│   │   ├── serializers.py       # API representation for models
│   │   ├── management/
│   │   │   ├── commands/
│   │   │   │   ├── seed.py      # Management command to seed the database
├── manage.py                    # Django project entry point
```

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/alx_travel_app_0x00.git
    cd alx_travel_app_0x00
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Seed the database with sample data:
    ```bash
    python manage.py seed
    ```

## Usage

1. Start the development server:
    ```bash
    python manage.py runserver
    ```
