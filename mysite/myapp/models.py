from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class SuggestionModel(models.Model):
    suggestion = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.suggestion

class CommentModel(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.ForeignKey(SuggestionModel, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s authored by %s" % (self.comment, self.author)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	score1 = models.IntegerField(default=0)
	score2 = models.IntegerField(default=0)
	score3 = models.IntegerField(default=0)
	scoreg = models.IntegerField(default=0)
	
	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()
        
        
        
