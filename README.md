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

## Usage

- **User Registration**: Users can create accounts to place orders and manage their profiles. 
  ![customer-resgister](https://github.com/htb2767/foodOnline/assets/91344736/f2391d45-4d34-472f-b552-b7ddbf58f5ee)
  When done with registration, customer will receive a confirmation email.
- **Vendor Registration**: Restaurants can apply for vendor status and submit their details for approval.
  ![vendor-resgister](https://github.com/htb2767/foodOnline/assets/91344736/449a693f-37db-4cb5-87d5-c499d20898da)
  When Vendor get approval for their registration, they will be notified via the email they signed up for.
- **Search for Restaurants**: Users can search for nearby restaurants and view their menus.
  ![search](https://github.com/htb2767/foodOnline/assets/91344736/9c1a798a-5f64-49a4-a1cb-117c0c8e8a56)
- **Order Food**: Users can add items to their cart and place orders.
  ![cart](https://github.com/htb2767/foodOnline/assets/91344736/b1428bcf-4a5d-4bfb-bfe9-f826d0edb156)
- **Checkout page**: The billing address will be  default information of customer
  ![checkout](https://github.com/htb2767/foodOnline/assets/91344736/4832476e-5968-4833-a94f-a80448a74e0d)
- **Order Detail**: when the payment went through, customer will be directed to order receipt
  ![order-receipt](https://github.com/htb2767/foodOnline/assets/91344736/a7267c21-9615-4b95-be80-5344979e5655)
- **Customer Dashboard**: View number of orders and updating profile:
  ![customer-dashboard](https://github.com/htb2767/foodOnline/assets/91344736/79fea872-8f4e-4b98-b4aa-c7733d334daa)
  ![profile-setting-c](https://github.com/htb2767/foodOnline/assets/91344736/daae926c-f8a0-4526-82aa-d133f1d9abc3)
- **Vendor Dashboard**: View number of orders and revenue, update profile, build menu and set open hour for restaurant
  +View number of orders and revenue
  ![vendor-dashbaord](https://github.com/htb2767/foodOnline/assets/91344736/db0904a0-4bb2-4fee-a806-1ddec07b8180)
  +Build menu
  ![build-menu](https://github.com/htb2767/foodOnline/assets/91344736/9679a650-12f2-412d-a59e-39d8e585d4c7)
  +Open Hour setting:
  ![openhour](https://github.com/htb2767/foodOnline/assets/91344736/97d99bcb-2844-4e2c-acb8-96013a59fdf6)









