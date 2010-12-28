#!/usr/bin/env python
# encoding: utf-8

import sys
import os

import csv

from parts.models import *
from django.core.exceptions import ObjectDoesNotExist

import datetime

def main():
    reader = csv.DictReader(open(sys.argv[1], 'Urb'))
    
    # {'Buyer': 'BRIAN LALOR',
    #  'Customer Part #': '',
    #  'Description': 'Phone Connectors PHONE 3.5MM STEREO  NON 161-3402',
    #  'Invoice #': '21779235',
    #  'Invoice Date (mm/dd/yyyy)': 'Dec 01, 2008',
    #  'Mfr.': 'Kobiconn',
    #  'Mfr. Part #': 'SCJ311M1NXS1B00G',
    #  'Mouser Part #': '161-3402-E',
    #  'Price': '$0.53',
    #  'Qty.': '5',
    #  'Sales Order #': '227347829',
    #  'Your PO #': '2474590'}
    
    try:
        distributor = Distributor.objects.get(name = sys.argv[2])
    except ObjectDoesNotExist:
        distributor = Distributor.objects.create(name = sys.argv[2])
    
    for row in reader:
        try:
            part = Part.objects.get(manufacturer = row['Mfr.'], part_num = row['Mfr. Part #'])
        except ObjectDoesNotExist:
            part = Part.objects.create(manufacturer = row['Mfr.'], part_num = row['Mfr. Part #'], description = row['Description'])
        
        try:
            dist_part = DistributorPart.objects.get(part = part, distributor = distributor)
        except ObjectDoesNotExist:
            dist_part = DistributorPart.objects.create(part = part, distributor = distributor, dist_part_num = row['Mouser Part #'])
        
        try:
            order = Order.objects.get(distributor = distributor, order_num = row['Invoice #'])
        except ObjectDoesNotExist:
            order = Order.objects.create(distributor = distributor, order_num = row['Invoice #'], order_date = datetime.date.today())
        
        try:
            line_item = LineItem.objects.get(order = order, distributor_part = dist_part)
        except ObjectDoesNotExist:
            line_item = LineItem.objects.create(order = order, distributor_part = dist_part, quantity = int(row['Qty.']), cost = 0)
            


if __name__ == '__main__':
    main()

