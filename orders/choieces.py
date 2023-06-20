from django.db import models



class SizeChoiece(models.TextChoices):
    SMALL='small'
    LARGE='large'
    EXTRA_LRAGE='extralarge'
    MEDIUM='medium'


class OrderStatus(models.TextChoices):
    PENDING='pending'
    IN_TRANSIT='inTransit'
    DELIVERED='delivered'