from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,
								on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	picture = models.ImageField(upload_to='users/%Y/%m/%d', default='images/default.jpeg', blank=True)
	GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
	phone_number = models.CharField(max_length=12, null=True)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)
