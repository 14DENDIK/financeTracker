from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from authentication.models import User


class IncomeType(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='income_types',
    )
    logo = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def set_deleted_income_type():
    return IncomeType.objects.get_or_create(name='deleted', logo='fas fa-trash')


def get_def():
    return IncomeType.objects.get_or_create(name='salary', logo='fas fa-money-bill')


class Income(models.Model):

    class Currencies(models.TextChoices):
        USD = 'usd', '$'
        # UZS = 'uzs', _('uzs')
        # RUB = 'rub', _('rub')

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='incomes',
    )
    type = models.ForeignKey(
        IncomeType,
        on_delete=models.SET(set_deleted_income_type),
        default=get_def
    )
    date = models.DateField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(
        max_length=5,
        choices=Currencies.choices,
        default=Currencies.USD
    )

    def __str__(self):
        return "%s - %s - %s" % (self.user.username, self.type.name, self.amount)


@receiver(post_save, sender=Income)
def add_to_total_income(sender, instance, created, *args, **kwargs):
    if created:
        user = instance.user
        user.total_income += instance.amount
        user.save()


@receiver(post_delete, sender=Income)
def minus_from_total_income(sender, instance, using, *args, **kwargs):
    user = instance.user
    user.total_income -= instance.amount
    user.save()
