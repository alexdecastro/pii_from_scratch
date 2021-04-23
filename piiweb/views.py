from django.shortcuts import render
from django.http import HttpResponse
from piidb.models import (Addresses, Participants, ParticipantsAddresses, SchoolLists, Sites)


# Create your views here.
def test_page(request):
    return HttpResponse('<h1>piiweb Test Page</h1>')


def addressSelectView(request, pguid_id):
    participants = Participants.objects.all()
    for part in participants:
        print("part.pguid: ", part.pguid)

    # Get addresses associated with pguid
    addr_id_list = []
    parts_addrs = ParticipantsAddresses.objects.filter(pguid=pguid_id)
    for part_addr in parts_addrs:
        addr_id_list.append(part_addr.address_id)
        unique_id = (part_addr.address_id, part_addr.pguid, part_addr.from_year, part_addr.to_year)
        print("part_addr.unique_id: ", unique_id)

    addresses = Addresses.objects.all()
    for addr in addresses:
        print("addr.addressid: ", addr.addressid)

    context = {
        'title': 'Address Select',
        'pguid': pguid_id,
        'addresses': addresses,
        'participants': participants,
        'parts_addrs': parts_addrs,
        'addr_id_list': addr_id_list,
    }
    return render(request, 'address-select.html', context)


def addressesView(request, pguid_id):
    participants = Participants.objects.all()
    for part in participants:
        print("part.pguid: ", part.pguid)

    # Get addresses associated with pguid
    addr_id_list = []
    parts_addrs = ParticipantsAddresses.objects.filter(pguid=pguid_id)
    for part_addr in parts_addrs:
        addr_id_list.append(part_addr.address_id)
        unique_id = (part_addr.address_id, part_addr.pguid, part_addr.from_year, part_addr.to_year)
        print("part_addr.unique_id: ", unique_id)

    addr_id_list = list(set(addr_id_list))
    addresses = Addresses.objects.all()
    for addr in addresses:
        print("addr.addressid: ", addr.addressid)

    context = {
        'title': 'Addresses',
        'addresses': addresses,
        'participants': participants,
        'parts_addrs': parts_addrs,
        'addr_id_list': addr_id_list,
    }
    return render(request, 'addresses.html', context)
