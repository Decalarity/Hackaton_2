from django.db import models
from applications.product.models import Product



class Cart(models.Model):
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.id,
                                               self.item,
                                               self.quantity,
                                               self.created_at,
                                               self.updated_at)


