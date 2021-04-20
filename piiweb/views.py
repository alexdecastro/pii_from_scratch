from django.shortcuts import render
from django.http import HttpResponse
from piidb.models import (Addresses, Participants, ParticipantsAddresses, SchoolLists, Sites)


# Create your views here.
def test_page(request):
    return HttpResponse('<h1>piiweb Test Page</h1>')


def participantsAddressesView(request, pguid_id):
    addresses = Addresses.objects.all()
    for addr in addresses:
        print("addr.addressid: ", addr.addressid)

    participants = Participants.objects.all()
    for part in participants:
        print("part.pguid: ", part.pguid)

    # Get addresses associated with pguid
    parts_addrs = ParticipantsAddresses.objects.filter(pguid=pguid_id)
    for part_addr in parts_addrs:
        unique_id = (part_addr.address_id, part_addr.pguid, part_addr.from_year, part_addr.to_year)
        print("part_addr.unique_id: ", unique_id)

    context = {
        'title': 'piiweb/views.py/participantsAddressesView()',
        'addresses': addresses,
        'participants': participants,
        'parts_addrs': parts_addrs,
    }
    return render(request, 'parts-addrs.html', context)


def addressesView(request, pguid_id):
    addresses = Addresses.objects.all()
    for addr in addresses:
        print("addr.addressid: ", addr.addressid)

    participants = Participants.objects.all()
    for part in participants:
        print("part.pguid: ", part.pguid)

    parts_addrs = ParticipantsAddresses.objects.all()
    for part_addr in parts_addrs:
        unique_id = (part_addr.address_id, part_addr.pguid, part_addr.from_year, part_addr.to_year)
        print("part_addr.unique_id: ", unique_id)

    context = {
        'title': 'piiweb/views.py/addressesView()',
        'addresses': addresses,
        'participants': participants,
        'parts_addrs': parts_addrs,
    }
    return render(request, 'addresses.html', context)
