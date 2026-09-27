from django.db import models
from django.conf import settings

class Ceremony(models.Model):
    CEREMONY_TYPES = [
        ('Wedding', 'Wedding'),
        ('Baptism', 'Baptism'),
        ('Funeral', 'Funeral'),
        ('Thanksgiving', 'Thanksgiving'),
        ('Bible Study', 'Bible Study'),
        ('Youth Meeting', 'Youth Meeting'),
        ('Other', 'Other'),
    ]

    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ceremony_type = models.CharField(max_length=50, choices=CEREMONY_TYPES)
    date = models.DateField()
    location = models.CharField(max_length=255)
    officiated_by = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ceremony_type} - {self.member.username} ({self.date})"
