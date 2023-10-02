# FoodOnline - Multi-Vendor Food Delivery Platform

A multi-vendor food delivery platform built with Python and Django.
## Installation and Setup

 Clone the repository:

```bash
git clone https://github.com/htb2767/foodOnline.git
```
```bash
Create a virtual environment and activate it:
cd food-online
python -m venv venv
source venv/bin/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Create a PostgreSQL database and update the database settings in settings.py.
Apply database migrations:
```bash
python manage.py migrate
```
Create a superuser for admin access:
```bash
python manage.py createsuperuser
```
Start the development server:
```bash
python manage.py runserver
```
#### Usage

Explain how users can interact with your platform, including user registration, vendor registration, and using the various features.
## Usage

- **User Registration**: Users can create accounts to place orders and manage their profiles.
  ![customer-resgister](https://github.com/htb2767/foodOnline/assets/91344736/f2391d45-4d34-472f-b552-b7ddbf58f5ee)
- **Vendor Registration**: Restaurants can apply for vendor status and submit their details for approval.
- **Search for Restaurants**: Users can search for nearby restaurants and view their menus.
- **Order Food**: Users can add items to their cart and place orders.
- **Admin Dashboard**: Admins can manage vendors, orders, and approve vendor applications.




