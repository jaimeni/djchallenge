from django.db import models


class Category(models.Model):
    name = models.CharField(
        'Name', max_length=225, null=False, blank=False, help_text='Name'
    )
    description = models.CharField(
        'Description', max_length=225, null=True, blank=True,
        help_text='Description'
    )

    class Meta:
        ordering = ('id', 'name')
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{name}'.format(name=self.name)
