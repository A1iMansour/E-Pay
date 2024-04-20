from rest_framework import serializers

class CurrencyConversionSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    from_currency = serializers.ChoiceField(choices=['USD', 'EUR', 'GBP'])
    to_currency = serializers.ChoiceField(choices=['USD', 'EUR', 'GBP'])
