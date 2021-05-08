from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView

from pii import settings
from piidb.models import (Addresses, Participants, ParticipantsAddresses, SchoolLists, Sites, TeacherSurvey)
from piiweb.forms import addressSelectForm, addressForm, participantForm, participantNewForm, teacherSurveyForm


def test_page(request):
    return HttpResponse('<h1>piiweb Test Page</h1>')


class teacherSurveyView(UpdateView):
    model = TeacherSurvey
    form_class = teacherSurveyForm
    slug_field = 'teachersurveyid'
    slug_url_kwarg = 'teachersurveyid'
    template_name = 'teacher-survey.html'


class participantView(UpdateView):
    model = Participants
    form_class = participantForm
    slug_field = 'pguid'
    slug_url_kwarg = 'pguid'
    template_name = 'participant-view.html'


class participantNewView(CreateView):
    model = Participants
    form_class = participantNewForm
    template_name = 'participant-view.html'


class addressView(UpdateView):
    model = Addresses
    form_class = addressForm
    slug_field = 'addressid' # database field
    slug_url_kwarg = 'addr_id' # slug name
    template_name = 'address-view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["GOOGLE_MAPS_API_KEY"] = settings.GOOGLE_MAPS_API_KEY
        return context


class addressNewView(CreateView):
    model = Addresses
    form_class = addressForm
    template_name = 'address-view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["GOOGLE_MAPS_API_KEY"] = settings.GOOGLE_MAPS_API_KEY
        return context


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


def addressesView1(request, pguid_id):
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
    return render(request, 'addresses1.html', context)


def addressesView2(request, pguid_id):
    if request.method == 'POST':
        print("DEBUG: views.py: addressesView2: request.POST: ", request.POST)
        if 'delete_id' in request.POST:
            delete_id = request.POST.get('delete_id')
            print("--> views.py: addressesView2: DELETE: delete_id:", delete_id)
            # Addresses.objects.filter(addressid=delete_id).delete()
            # ParticipantsAddresses.objects.filter(address_id=delete_id).delete()

        form = addressSelectForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            new_input = form.save()

    else:
        print("DEBUG: views.py: addressesView2: request.GET: ", request.GET)
        form = addressSelectForm()

    # Create an array of address ids associated with this pguid
    addr_id_list = []
    parts_addrs = ParticipantsAddresses.objects.filter(pguid=pguid_id)
    for part_addr in parts_addrs:
        addr_id_list.append(part_addr.address_id)
    addr_id_list = list(set(addr_id_list))

    addresses = Addresses.objects.all()

    context = {
        'title': 'Address List',
        'pguid': pguid_id,
        'addresses': addresses,
        'parts_addrs': parts_addrs,
        'addr_id_list': addr_id_list,
    }
    return render(request, 'addresses2.html', context)


@csrf_exempt
def create_part_addr(request, pguid_id, addr_id):
    print("--> views.py: create_part_addr: pguid_id: ", pguid_id, " addr_id: ", addr_id)
    to_year = datetime.now().year
    from_year = to_year - 1
    participant = Participants.objects.get(pguid=pguid_id)
    obj, created = ParticipantsAddresses.objects.update_or_create(
        pguid=participant, address_id=addr_id,
        defaults={'from_year': from_year, 'to_year': to_year,
                  'addresstype': "primary", 'percentoftime': 100}
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


def addressNewViewForPguid(request, pguid_id):

    participant = Participants.objects.get(pguid=pguid_id)

    model = Addresses
    form_class = addressForm

    template_name = 'address-view.html'

    l = request.user.groups.values_list('name',flat = True)
    groups = list(l)
    ids = []
    for group in groups:
        ids += [x['pguid'] for x in Participants.objects.filter(current_site=group).values('pguid')]

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        print("Form Posted")
        # Create a form instance and populate it with data from the request (binding):
        form = addressForm(request.POST, pguid_id)

        # Check if the form is valid:
        if form.is_valid():
            print("Form is valid")

            # process the data in form.cleaned_data as required
            print("addressNewViewForPguid: form.cleaned_data: ", form.cleaned_data)
            addressid = form.cleaned_data['addressid']
            streetnumber = form.cleaned_data['streetnumber']
            streetname = form.cleaned_data['streetname']
            aptnumber = form.cleaned_data['aptnumber']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            google_place_id = form.cleaned_data['google_place_id']
            google_result = form.cleaned_data['google_result']
            google_latitude = form.cleaned_data['google_latitude']
            google_longitude = form.cleaned_data['google_longitude']

            obj, created = Addresses.objects.update_or_create(
                addressid=addressid,
                streetnumber=streetnumber,
                streetname=streetname,
                aptnumber=aptnumber,
                city=city,
                state=state,
                zipcode=zipcode,
                google_place_id=google_place_id,
                google_latitude=google_latitude,
                google_longitude=google_longitude,
            )

            to_year = datetime.now().year
            from_year = to_year - 1
            obj, created = ParticipantsAddresses.objects.update_or_create(
                pguid=participant, address_id=addressid,
                defaults={'from_year': from_year, 'to_year': to_year,
                          'addresstype': "primary", 'percentoftime': 100}
            )

            # redirect to a new URL:
            #return render(request,'address-view.html')
            #return HttpResponseRedirect(reverse('addresses'))

        else:
            print("ERROR: addressNewViewForPguid: form.errors: ", form.errors)
            exit(1)

    else:
        print("Form Get")
        form = addressForm(instance=participant)

    context = {
        'form': form, 'groups': ', '.join(groups),
        'ids': ids,
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    }

    return render(request, template_name, context)
