from django.db import models


class TicketStatus(models.Model):
    code = models.CharField('Код', max_length=16, primary_key=True)
    name = models.CharField('Название', max_length=32)

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return f'{self.code} ({self.name})'

