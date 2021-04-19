from django.shortcuts import render
from django.http import HttpResponse
from piidb.models import (Addresses, Participants, ParticipantsAddresses, SchoolLists, Sites)


# Create your views here.
def test_page(request):
    return HttpResponse('<h1>piiweb Test Page</h1>')


def test_template(request):
    addresses = Addresses.objects.all()
    for addr in addresses:
        print("addr.addressid: ", addr.addressid)

    participants = Participants.objects.all()
    for part in participants:
        print("part.pguid: ", part.pguid)

    part_addrs = ParticipantsAddresses.objects.all()
    for part_addr in part_addrs:
        unique_id = (part_addr.address_id, part_addr.pguid, part_addr.from_year, part_addr.to_year)
        print("part_addr.unique_id: ", unique_id)

    context = {
        'title': 'Test Template',
        'addresses': addresses,
        'participants': participants,
        'part_addrs': part_addrs,
    }
    return render(request, 'test_template.html', context)
