from django.db import models

# Create your models here.
class Token(models.Model):
	token = models.CharField(max_length=200, blank=True, null=True, verbose_name="Access Token")
	refresh_token = models.CharField(max_length=200, blank=True, null=True, verbose_name="Refresh Token")
	hora_atualizacao = models.TimeField(blank=True, null=True,)

	def __str__(self):
		return u'%s' % (self.token)

	def save(self, *args, **kwargs):
		if self.__class__.objects.count():
			self.pk = self.__class__.objects.first().pk
		super().save(*args, **kwargs)

	class Meta:
		verbose_name = "Token"
		verbose_name_plural = "Tokens"
