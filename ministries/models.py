# ministries/models.py

from django.db import models
from django.conf import settings

# Use Member model if you prefer linking to Member, else link to user
# We'll link to the User model for leader, and allow many members via M2M.
# TEST: file created

class Ministry(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    description = models.TextField(blank=True)
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='led_ministries')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='ministries')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Optional: store join requests from users (admin can approve)
class MembershipRequest(models.Model):
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE, related_name='join_requests')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('ministry', 'user')

    def __str__(self):
        return f"{self.user} -> {self.ministry} ({'approved' if self.approved else 'pending'})"

# TEST: run makemigrations to see new migrations for ministries


# Create your models here.
