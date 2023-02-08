from django.db import models
from django.core.validators import RegexValidator

class Maillist(models.Model):   
    text = models.TextField()
    start = models.DateTimeField(verbose_name="Creation Start date")
    end = models.DateTimeField(verbose_name='Creation End date')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    phone = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Client(models.Model):   
    phone_regex = RegexValidator(regex=r'([7]){1}([\d]){10}', message="Phone number must be entered in the format: '7XXXXXXXXXX'. Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, unique=True)
    tag = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=40, blank=True)
    joined = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering=('id',)

    def __str__ (self):
        return self.phone_number

class Message(models.Model):   
    date = models.DateTimeField()
    status = models.BooleanField(default=False)
    maillist = models.OneToOneField(Maillist, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.maillist)    