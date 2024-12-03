from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TicketStatus(models.Model):
    code = models.CharField('Код', max_length=16, primary_key=True)
    name = models.CharField('Название', max_length=32)

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return f'{self.code} ({self.name})'


class Ticket(models.Model):
    client = models.ForeignKey(User, models.SET_NULL, 'tickets',
                               null=True, verbose_name='Клиент')
    status = models.ForeignKey(TicketStatus, models.RESTRICT,
                               'tickets', verbose_name='Статус')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    manager = models.ForeignKey(User, models.SET_NULL, 'tickets',
                                null=True, verbose_name='Менеджер')

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return f'Обращение №{self.pk} - {self.status}'
