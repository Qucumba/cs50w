from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}: {self.description}"

class Bid(models.Model):
    rel_listing = models.ForeignKey(Listing, on_delete=models.PROTECT)
    starting_bid = models.DecimalField(max_digits=9, decimal_places=2)
    current_bid = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.rel_listing.title}: Starting bid {self.starting_bid}/Current bid {self.current_bid}"

class Comment(models.Model):
    rel_listing = models.ForeignKey(Listing, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f"Listing: {self.rel_listing.title} /n Comment: {self.text}"