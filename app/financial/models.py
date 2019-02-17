from django.db import models


class FinancialType(models.Model):
    created_at = models.DateTimeField()
    name = models.TextField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Financial(models.Model):
    created_at = models.DateTimeField()
    name = models.TextField()
    value = models.FloatField()
    type = models.ForeignKey(FinancialType, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at', 'name')
