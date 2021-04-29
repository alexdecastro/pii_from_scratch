from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from piidb.models import (Addresses, Participants, ParticipantsAddresses, SchoolLists, Sites)
from piiweb.forms import addressSelectForm


def test_page(request):
    return HttpResponse('<h1>piiweb Test Page</h1>')


def addressSelectView(request, pguid_id):
    if request.method == 'POST':
        print("DEBUG: views.py: addressSelectView: request.POST: ", request.POST)
        if 'delete_id' in request.POST:
            delete_id = request.POST.get('delete_id')
            print("--> views.py: addressSelectView: DELETE: delete_id:", delete_id)
            # Addresses.objects.filter(addressid=delete_id).delete()
            # ParticipantsAddresses.objects.filter(address_id=delete_id).delete()

        form = addressSelectForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            new_input = form.save()

    else:
        print("DEBUG: views.py: addressSelectView: request.GET: ", request.GET)
        form = addressSelectForm()

    # Create an array of address ids associated with this pguid
    addr_id_list = []
    parts_addrs = ParticipantsAddresses.objects.filter(pguid=pguid_id)
    for part_addr in parts_addrs:
        addr_id_list.append(part_addr.address_id)
    addr_id_list = list(set(addr_id_list))

    addresses = Addresses.objects.all()

    context = {
        'title': 'Address Select',
        'pguid': pguid_id,
        'addresses': addresses,
        'parts_addrs': parts_addrs,
        'addr_id_list': addr_id_list,
    }
    return render(request, 'address-select.html', context)


def addressesView(request, pguid_id):
    participants = Participants.objects.all()
    for part in participants:
        print("part.pguid: ", part.pguid)

    # Create an array of address ids associated with this pguid
    addr_id_list = []
    parts_addrs = ParticipantsAddresses.objects.filter(pguid=pguid_id)
    for part_addr in parts_addrs:
        addr_id_list.append(part_addr.address_id)
    addr_id_list = list(set(addr_id_list))

    addresses = Addresses.objects.all()

    context = {
        'title': 'Addresses',
        'addresses': addresses,
        'participants': participants,
        'parts_addrs': parts_addrs,
        'addr_id_list': addr_id_list,
    }
    return render(request, 'addresses.html', context)


@csrf_exempt
def create_part_addr(request, pguid_id, addr_id):
    print("--> views.py: create_part_addr: pguid_id: ", pguid_id, " addr_id: ", addr_id)
    from_year = 2000
    to_year = 2002
    address_type = "primary"
    percentoftime = 100
    participant = Participants.objects.get(pguid=pguid_id)
    obj, created = ParticipantsAddresses.objects.update_or_create(
        pguid=participant, address_id=addr_id,
        defaults={'from_year': from_year, 'to_year': to_year,
                  'addresstype': address_type, 'percentoftime': percentoftime}
    )
    response = {
        'ok': True,
        'pguid_id': pguid_id,
        'addr_id': addr_id,
    }
    return JsonResponse(response)


@csrf_exempt
def delete_part_addr(request, pguid_id, addr_id):
    print("--> views.py: delete_part_addr: pguid_id: ", pguid_id, " addr_id: ", addr_id)
    ParticipantsAddresses.objects.filter(pguid_id=pguid_id, address_id=addr_id).delete()
    response = {
        'ok': True,
        'pguid_id': pguid_id,
        'addr_id': addr_id,
    }
    return JsonResponse(response)
