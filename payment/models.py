from django.db import models


class Payment(models.Model):
    number = models.PositiveIntegerField()
    date = models.DateField()
    sum = models.IntegerField(help_text="amount in cents")
    purpose_of_payment = models.CharField(max_length=255)
    status = models.ForeignKey("Status", on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
