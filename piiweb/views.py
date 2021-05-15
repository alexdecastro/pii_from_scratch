from datetime import datetime

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
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


class addressView1(UpdateView):
    model = Addresses
    form_class = addressForm
    slug_field = 'addressid' # database field
    slug_url_kwarg = 'addr_id' # slug name
    template_name = 'address-view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["GOOGLE_MAPS_API_KEY"] = settings.GOOGLE_MAPS_API_KEY
        return context


class addressNewView1(CreateView):
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
            Addresses.objects.filter(addressid=delete_id).delete()
            ParticipantsAddresses.objects.filter(address_id=delete_id).delete()

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


def addressesViewOld(request):
    l = request.user.groups.values_list('name',flat = True)
    name = request.user.get_full_name()
    groups = list(l)
    ids = []
    for group in groups:
        ids += [x['pguid'] for x in Participants.objects.filter(current_site=group).values('pguid')]
    context ={
        'groups': ', '.join(groups), 'ids': ids, 'name': name,
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'addresses-old.html', context)


def addressesView(request):
    if request.method == 'POST':
        print("DEBUG: views.py: addressesView: request.POST: ", request.POST)
        if 'delete_id' in request.POST:
            delete_id = request.POST.get('delete_id')
            print("--> views.py: addressesView: DELETE: delete_id:", delete_id)
            ParticipantsAddresses.objects.filter(address_id=delete_id).delete()
            Addresses.objects.filter(addressid=delete_id).delete()

        form = addressSelectForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            new_input = form.save()

    else:
        print("DEBUG: views.py: addressesView: request.GET: ", request.GET)
        form = addressSelectForm()

    addresses = Addresses.objects.all()

    context = {
        'title': 'Address List',
        'addresses': addresses,
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'addresses.html', context)


@csrf_exempt
def create_part_addr(request, pguid_id, addr_id):
    print("--> views.py: create_part_addr: pguid_id: ", pguid_id, " addr_id: ", addr_id)
    next_year = max([x['to_year'] for x in ParticipantsAddresses.objects.filter(pguid=pguid_id).values('to_year')], default=datetime.now().year) + 1
    print(next_year)
    from_year = next_year
    to_year = next_year
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


def addressNewView(request):
    return addressEditView(request, None)


# Similar to: objects.get() except this returns None if the object does not exist
# Replace: Addresses.get(addressid=addr_id)
#    with: get_if_exists(Addresses, addressid=addr_id)
def get_if_exists(model, **kwargs):
    try:
        obj = model.objects.get(**kwargs)
    except model.DoesNotExist:  # Be explicit about exceptions
        obj = None
    return obj


def addressEditView(request, addr_id):

    address = None
    if addr_id != None:
        address = get_if_exists(Addresses, addressid=addr_id)

    model = Addresses
    form_class = addressForm
    template_name = 'address-view.html'

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        print("--> views.py: addressEditView: Form Posted")
        # Create a form instance and populate it with data from the request (binding):
        form = addressForm(request.POST, instance=address)

        # Check if the form is valid:
        if form.is_valid():
            print("--> views.py: addressEditView: form.cleaned_data: ", form.cleaned_data)

            # process the data in form.cleaned_data as required
            addressid = form.cleaned_data['addressid']

            streetnumber = form.cleaned_data['streetnumber']
            google_streetnumber = streetnumber

            streetname = form.cleaned_data['streetname']
            google_streetname = streetname

            aptnumber = form.cleaned_data['aptnumber']

            city = form.cleaned_data['city']
            google_city = city

            state = form.cleaned_data['state']
            google_state = state

            zipcode = form.cleaned_data['zipcode']
            google_zipcode = zipcode
            google_zipsuffix = form.cleaned_data['google_zipsuffix']

            google_neighborhood = form.cleaned_data['google_neighborhood']
            google_county = form.cleaned_data['google_county']
            google_country = form.cleaned_data['google_country']

            google_place_id = form.cleaned_data['google_place_id']
            google_latitude = form.cleaned_data['google_latitude']
            google_longitude = form.cleaned_data['google_longitude']

            google_query = form.cleaned_data['google_query']
            google_result = form.cleaned_data['google_result']

            google_status = "OK"
            google_method = "google"
            google_date = datetime.now()
            google_googlesenttoredcap = False
            google_elevation = None

            if addr_id != None:
                # If editing an existing address, delete it first
                Addresses.objects.filter(addressid=addressid).delete()

            obj, created = Addresses.objects.update_or_create(
                addressid=addressid,
                streetnumber=streetnumber, google_streetnumber=google_streetnumber,
                streetname=streetname, google_streetname=google_streetname,
                aptnumber=aptnumber,
                city=city, google_city=google_city,
                state=state, google_state=google_state,
                zipcode=zipcode, google_zipcode=google_zipcode, google_zipsuffix=google_zipsuffix,
                google_neighborhood=google_neighborhood, google_county=google_county, google_country=google_country,
                google_place_id=google_place_id,
                google_latitude=google_latitude, google_longitude=google_longitude,
                google_query=google_query, google_result=google_result,
                google_status=google_status, google_method=google_method, google_date=google_date,
                google_googlesenttoredcap=google_googlesenttoredcap,
                google_elevation=google_elevation,
            )

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('addressEditView', args=[str(addressid)]))

        else:
            print("ERROR: addressEditView: form.errors: ", form.errors)

    else:
        print("--> views.py: addressEditView: Form Get")
        form = addressForm(instance=address)

    context = {
        'form': form,
        'addr_id': addr_id,
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, template_name, context)
