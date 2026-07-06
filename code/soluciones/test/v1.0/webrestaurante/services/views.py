from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from services.models import Service
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ServiceForm, OrderForm
from django.views.decorators.http import require_POST
import json
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

@staff_member_required()
# @permission_required('services.change_service', raise_exception=True)
def create(request):
    if not request.user.has_perm('services.change_service'):
        raise PermissionDenied('No tienes los privilegios suficientes')
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/services')
    else:
        form = ServiceForm()
    return render(request, 'services/service_create.html', {'form':form})

@staff_member_required()
def update(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/services')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/service_update.html', {'form':form})

@staff_member_required()
def delete(request, service_id):
    service = Service.objects.get(id=service_id)
    service.delete()
    return HttpResponseRedirect('/services')

@require_POST
def order_request(request):
    order = list()
    total = 0
    try:        
        data_order = json.loads(request.POST['data_order'])
        for key, qty in data_order.items():
            detail = {}
            service = Service.objects.get(pk=int(key))
            detail['title'] = service.title
            detail['cost'] = float(service.cost)
            detail['qty'] = qty            
            detail['sub_total'] = float(service.cost) * qty
            total += detail['sub_total']
            order.append(detail)
    except json.JSONDecodeError as e:
        print(f"Error parsing. Details: {e}")                
    request.session['total_order'] = total
    request.session['detail_order'] = order
    return render(request, 'services/detail_order.html', {'order':order, 'total':total})

def order_create(request):
    # Get total
    total = request.session.get('total_order')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('services:thanks'))            
    else:  # Método get
        form = OrderForm(initial={'total':total})
    return render(request, 'services/order_create.html', {'form': form})

def order_thanks(request):
    return render(request, 'services/order_thanks.html')