# app/fees/serializers.py
from rest_framework import serializers
from .models import Fee, Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'fee', 'amount', 'date']

class FeeSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Fee
        fields = ['id', 'student', 'amount_due', 'due_date', 'amount_paid', 'status', 'transactions']
