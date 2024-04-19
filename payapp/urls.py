from . import views
from django.urls import path

urlpatterns = [
    



     path('payment/', views.pay, name='payfunc'),
     path('request/', views.request, name='requestfunc'),
     path('requestsuccess/', views.request_success, name='request_success'),
     path('paymentsuccess/', views.pay_success, name='pay_success'),
     path('fetch_notifications/', views.fetch_notifications, name='fetch_notifications'),
     path('mark_notification_seen/', views.mark_notification_seen, name='mark_notification_seen'),

]