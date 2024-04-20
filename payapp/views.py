from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Request, Payment
from register.models import Usermoney
from .forms import RequestForm, PaymentForm
from .models import Notify
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages

def mark_notification_seen(request):
    if request.method == 'POST':
        notification_ids = request.POST.getlist('notification_ids')
        user_notifications = Notify.objects.filter(pk__in=notification_ids, user=request.user, seen=False)
        user_notifications.update(seen=True)
        return HttpResponse("Notifications marked as seen successfully.")
    else:
        return HttpResponse(status=405) 
    
def userpayments(request):
    user_payments = Payment.objects.filter(userfrom=request.user) | Payment.objects.filter(userto=request.user)
    return render(request, 'transaction.html', {'user_payments': user_payments})


def fetch_notifications(request):
    user_notifications = Notify.objects.filter(user=request.user, seen=False)
   
    #print(request.user)
    return render(request, 'notifications_partial.html', {'notifications': user_notifications})


def create_notification(sender, receiver, message):
    Notify.objects.create(user=receiver, message=message, seen=False)

@login_required
def request_success(request):
    return render(request, 'requestsuc.html')

@login_required
def request(request):
    user_money = Usermoney.objects.get(user=request.user)
    balance = user_money.balance
    currency= user_money.get_currency_display()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            user_to_username = form.cleaned_data['userto']
            user_to = User.objects.get(username=user_to_username)
            payment = form.cleaned_data['payment']
            currency = form.cleaned_data['currency']
            Request.objects.create(userfrom=request.user, userto=user_to, payment=payment, currency=currency)
            message = f'{request.user.username} requested {payment} {currency}from you.'
            create_notification(request.user, user_to, message) 
            return redirect('request_success')
    
    else:
        form = RequestForm()
    context = {'form': form, 'balance': balance, 'currency':currency}
    return render(request, 'request.html',  context)


@login_required
def pay(request):
    user_money = Usermoney.objects.get(user=request.user)
    balance = user_money.balance
    currency= user_money.get_currency_display()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            user_to_username = form.cleaned_data['userto']
            paymentdone= form.cleaned_data['payment']
            if paymentdone > balance:
               
                messages.error(request, 'Insufficient balance for this payment.')
                return render(request, 'payment.html', {'form': form, 'balance': balance, 'currency': currency})

            try:
                receiver_user = User.objects.get(username=user_to_username)
            except User.DoesNotExist:
                
                messages.error(request, 'Receiver user does not exist.')
                return render(request, 'payment.html', {'form': form, 'balance': balance, 'currency': currency})
            recieverbalance = Usermoney.objects.get(user=receiver_user)

            recieverbalance.balance +=paymentdone
            recieverbalance.save()
            user_money.balance-=paymentdone
            user_money.save()
            
            new_request = form.save(commit=False)
            new_request.userfrom = request.user.username
            new_request.save()
            return redirect('pay_success')
    else:
        form = PaymentForm()

    context = {'form': form, 'balance': balance, 'currency':currency}
    return render(request, 'payment.html', context)

@login_required
def pay_success(request):
    return render(request, 'paidsuc.html')




