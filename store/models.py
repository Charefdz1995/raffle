from django.db import models
import uuid

class product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.IntegerField()
    spot_price = models.IntegerField()

class customer(models.Model):
    full_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)

class spot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_ref = models.ForeignKey(product, on_delete = models.CASCADE)
    customer_ref = models.ForeignKey(customer,on_delete = models.CASCADE)

class raffle(models.Model):
    product_ref = models.ForeignKey(product, on_delete = models.CASCADE)
    raffle_time = models.DateTimeField()
    raffle_winner = models.ForeignKey(customer,on_delete = models.CASCADE)

    def getWinner(self):
        pass

