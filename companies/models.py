from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    annual_revenue = models.FloatField()
    employee_count = models.IntegerField()
    compliance_score = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields = ['industry']),
            models.Index(fields=['annual_revenue']),
            models.Index(fields=['is_active'])
        ]

    def __str__(self):
        return self.name


class CompanyScore(models.Model):
    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        related_name='score'
    )

    total_score = models.FloatField()
    rank = models.IntegerField(null=True , blank=True)
    calculated_at = models.DateTimeField(auto_now = True) 

    class Meta:
        indexes = [
            models.Index(fields=['total_score']),
            models.Index(fields=['rank']),
        ]

        def __str__(self):
            return f"{self.company.name} - Score: {self.total_score}" 