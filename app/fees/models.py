#app/fees/models.py
from django.db import models

class Fee(models.Model):
    student = models.ForeignKey('enrollment.Student', on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()

    @property
    def amount_paid(self):
        return self.transactions.aggregate(total=models.Sum('amount'))['total'] or 0

    @property
    def status(self):
        if self.amount_paid >= self.amount_due:
            return 'PAID'
        elif self.amount_paid > 0:
            return 'PARTIAL'
        return 'UNPAID'

    def __str__(self):
        return f"Fee for {self.student} - Due: {self.amount_due}, Paid: {self.amount_paid}"

class Transaction(models.Model):
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.fee.student} - Amount: {self.amount}"
