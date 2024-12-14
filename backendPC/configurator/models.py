from django.db import models

class Case(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name

class PowerSupply(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name

class Motherboard(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name

class RAM(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name

class GPU(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name

class CPU(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name

class HardDrive(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name
from django.db import models

class Case(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name

class PowerSupply(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name

class Motherboard(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name

class RAM(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name

class GPU(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name

class CPU(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name

class HardDrive(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.TextField()

    def __str__(self):
        return self.name
