# encoding: utf-8

from django.db import models

class Distributor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __unicode__(self):
        return self.name
    


class Classification(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    


class StorageLocation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name
    


class Part(models.Model):
    manufacturer = models.CharField(max_length=200)
    part_num = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    value = models.CharField(max_length=200, blank=True)
    classification = models.ForeignKey(Classification, null=True, blank=True)
    storage_location = models.ManyToManyField(StorageLocation, null=True, blank=True)
    
    def __unicode__(self):
        return self.part_num
    


# should have a composite unique key (part, distributor), but Django doesn't support that…
class DistributorPart(models.Model):
    part = models.ForeignKey(Part)
    distributor = models.ForeignKey(Distributor)
    dist_part_num = models.CharField(max_length=200)
    
    def __unicode__(self):
        return u'%s %s (%s)' % (self.distributor, self.dist_part_num, self.part)
    


# should have a composite unique key (distributor, order_num)
class Order(models.Model):
    distributor = models.ForeignKey(Distributor)
    order_num = models.CharField(max_length=50)
    order_date = models.DateField()
    
    def __unicode__(self):
        return self.order_num
    


class LineItem(models.Model):
    order = models.ForeignKey(Order)
    distributor_part = models.ForeignKey(DistributorPart)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __unicode__(self):
        return u'%s %s' % (self.order.order_num, self.distributor_part.dist_part_num)
    


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
    

