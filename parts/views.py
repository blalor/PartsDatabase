# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

import django.template as template

from parts.models import Order, Part, LineItem

def index(request):
    return render_to_response('parts/index.html')


def list_orders(request):
    order_list = Order.objects.all().order_by('order_date')
    
    return render_to_response('parts/orders.html', {'order_list': order_list})


def list_parts(request):
    part_list = Part.objects.all()
    
    return render_to_response('parts/parts.html', {'part_list': part_list})


def order_detail(request, order_id):
    order = Order.objects.get(id = order_id)
    
    return render_to_response('parts/order_detail.html', {'order': order})


def part_detail(request, part_id):
    part = Part.objects.get(id = part_id)
    orders = []
    
    for dist_part in part.distributorpart_set.all():
        for line_item in LineItem.objects.filter(distributor_part = dist_part):
            orders.append(line_item.order)
        
    
    return render_to_response(
        'parts/part_detail.html',
        {
            'part': part,
            'orders': orders,
        }
    )

