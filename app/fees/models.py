from django.db import models
from app.enrollment.models import Student

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('PAID', 'Paid'), ('PARTIAL', 'Partial'), ('UNPAID', 'Unpaid')])

    def __str__(self):
        return f"Fee for {self.student} - Due: {self.amount_due}, Paid: {self.amount_paid}"
