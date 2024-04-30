# <E-Pay>

## Description
This project implements a simplified online payment system similar to PayPal, built using the Django framework. 
Users can send and request money from each other, manage their accounts, and view transaction history. 
An admin interface provides access to all user data and transactions.

**Features:**

1. User registration, login/logout
2. Send and request money between registered users
3. Secure admin interface for registering new admins and accessing all user info and transactions
4. Support for different currencies (with currency conversion)

## Installation

1)Clone this repository: 
git clone https://github.com/A1iMansour/E-Pay.git
2)Create a virtual environment and activate it (recommended).
3) install dependencies:
pip install -r requirements.txt
4)Create a superuser account (optional, for admin access):
python manage.py createsuperuser
5)Start the development server:
python manage.py runserver

## Usage

1. Access the application in your web browser at http://127.0.0.1:8000/ (default development server address).
2. Register for an account or login if you already have one.
3. Use the provided functionalities to send/request money, view transactions, and manage your account.
  (To log in to multiple user accounts simultaneously, use either a different web browser or a private window in your existing browser.)
4. For admin access, use the credentials created during superuser creation.


