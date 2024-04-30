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

## Setup

### Installation

1. **Clone this repository:** `git clone https://github.com/A1iMansour/E-Pay.git`
2. **Create a virtual environment and activate it (recommended).**
3. **Install dependencies:** `pip install -r requirements.txt`
4. **Create a superuser account (optional, for admin access):** `python manage.py createsuperuser`
5. **Start the development server:** `python manage.py runserver`


### Usage

1. **Access the Application:** Open your web browser and navigate to http://127.0.0.1:8000/ (default development server address).
2. **Register/Login:** Create an account if you're a new user or log in if you already have an account.
3. **Functionality Overview:**
   - Send/Request Money: Use the provided features to send or request money between registered users.
   - View Transactions: Access your transaction history to track payments and receipts.
   - Account Management: Manage your account settings and preferences.
   - Multiple Sessions: To log in with multiple user accounts simultaneously, use a different web browser or a private window in your existing browser.
4. **Admin Access:** If you have admin privileges (created during superuser setup), log in to access administrative features such as user management and transaction monitoring.



