from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CurrencyConversionSerializer

exchange_rates = {
    'EUR': {'USD': 1.07, 'GBP': 0.86},
    'USD': {'EUR': 0.93, 'GBP': 0.81},
    'GBP': {'EUR': 1.16, 'USD': 1.23},
}
@api_view(['GET'])
def convert_currency(request):
    serializer = CurrencyConversionSerializer(data=request.query_params)
    if serializer.is_valid():
        amount = serializer.validated_data['amount']
        from_currency = serializer.validated_data['from_currency']
        to_currency = serializer.validated_data['to_currency']

        exchange_rates = {
            'USD': {'EUR': 0.93, 'GBP': 0.81, 'USD':1},
            'EUR': {'USD': 1.07, 'GBP': 0.86, 'EUR':1},
            'GBP': {'USD': 1.23, 'EUR': 1.16, 'GBP':1},
        }

        if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
            rate = exchange_rates[from_currency][to_currency]
            converted_amount = amount * rate
            return Response({'converted_amount': converted_amount})

        return Response({'error': 'Invalid currency pair.'}, status=400)

    return Response(serializer.errors, status=400)
