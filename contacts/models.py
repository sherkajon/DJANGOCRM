from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    website = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    designation = models.CharField(max_length=60)
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)



