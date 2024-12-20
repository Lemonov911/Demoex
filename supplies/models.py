from django.db import models
from accounts.models import Role


class Supplies(models.Model):
    name = models.CharField(
        'название',
        max_length=100,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Application(models.Model):
    client = models.ForeignKey(
        'accounts.User',
        related_name='my_applications',
        verbose_name='клиент',
        on_delete=models.CASCADE,
        limit_choices_to={'role': Role.CLIENT},
    )
    manager = models.ForeignKey(
        'accounts.User',
        related_name='client_apps',
        verbose_name='менеджер',
        on_delete=models.CASCADE,
        limit_choices_to={'role': Role.MANAGER},
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'Заявка № {self.pk}'

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'заявки на поставку'


class Item(models.Model):
    item = models.ForeignKey(
        'supplies.Supplies',
        verbose_name='Товар',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    application = models.ForeignKey(
        'Application',
        verbose_name='заявка',
        on_delete=models.CASCADE,
    )
    number = models.PositiveIntegerField(
        'Количество',
        default=1,
    )
    def __str__(self):
        return f'{self.item}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
