/*
Handle multiple Google Maps in one page.
For each map, create HTML elements with prefix: 'id_prefix'

<input type="text" id="id_streetnumber" disabled="">
<input type="text" id="id_streetname" disabled="">
<input type="text" id="id_city" disabled="">
<input type="text" id="id_state" disabled="">
<input type="text" id="id_zipcode" disabled="">
<input type="text" id="id_address_search">
<input type="text" id="id_addressid">
<input type="text" id="id_google_place_id">
<input type="text" id="id_google_latitude">
<input type="text" id="id_google_longitude">
<div>
    <div id="id_google_map"></div>
    <style>#id_google_map {height: 400px; margin:0px}</style>
</div>

<script src="{% static 'vendor/jquery/jquery-3.5.1.min.js' %}"></script>
<script src="https://maps.googleapis.com/maps/api/js?v=weekly&libraries=places&key=GOOGLE_MAPS_API_KEY"></script>
<script src="{% static 'js/address-view.js' %}"></script>
 */

$(document).ready(function() {
    initializeGoogleMap("id");
    markAddressOnMap('id_google_map', addressFromAddressFields("id"));

    $('form').submit(function(e) {
        // Enable the address fields so they will be saved
        $('.enable_save').each(function (e) {
            $(this).removeAttr('disabled');
        })
    });
    $('#id_ddresses').on('click', function (e) {
        var url = '/pii/addresses/';
        location.href = url;
    });
});

function addressFromAddressFields(id_prefix) {
    let streetnumber = $('#'+id_prefix+'_streetnumber').val();
    let streetname = $('#'+id_prefix+'_streetname').val();
    let city = $('#'+id_prefix+'_city').val();
    let state = $('#'+id_prefix+'_state').val();
    let zipcode = $('#'+id_prefix+'_zipcode').val();
    return streetnumber.concat(" ", streetname, " ", city, " ", state, " ", zipcode);
}

function initializeGoogleMap(id_prefix) {

    // Disable the address fields since they will be automatically filled in
    $('#'+id_prefix+'_streetnumber').prop('disabled', true);
    $('#'+id_prefix+'_streetnumber').addClass("enable_save");
    $('#'+id_prefix+'_streetname').prop("disabled", true);
    $('#'+id_prefix+'_streetname').addClass("enable_save");
    $('#'+id_prefix+'_city').prop("disabled", true);
    $('#'+id_prefix+'_city').addClass("enable_save");
    $('#'+id_prefix+'_state').prop("disabled", true);
    $('#'+id_prefix+'_state').addClass("enable_save");
    $('#'+id_prefix+'_zipcode').prop("disabled", true);
    $('#'+id_prefix+'_zipcode').addClass("enable_save");
    $('#'+id_prefix+'_addressid').prop("disabled", true);
    $('#'+id_prefix+'_addressid').addClass("enable_save");
    $('#'+id_prefix+'_google_place_id').prop("disabled", true);
    $('#'+id_prefix+'_google_place_id').addClass("enable_save");
    $('#'+id_prefix+'_google_latitude').prop("disabled", true);
    $('#'+id_prefix+'_google_latitude').addClass("enable_save");
    $('#'+id_prefix+'_google_longitude').prop("disabled", true);
    $('#'+id_prefix+'_google_longitude').addClass("enable_save");

    let id = id_prefix+"_address_search";
    let autocomplete = new google.maps.places.Autocomplete(document.getElementById(id));
    google.maps.event.addListener(autocomplete, 'place_changed', function () {

        var place = autocomplete.getPlace();
        if (typeof place.formatted_address === 'undefined') {
            alert("place.formatted_address is undefined");
            return;
        }

        var geocodeDetails = {};
        geocodeDetails['results'] = [place];
        geocodeDetails['status'] = "OK";
        console.log("geocodeDetails:");
        console.table(geocodeDetails);

        if ($('#'+id_prefix+'_addressid').val() === "") {
            $('#'+id_prefix+'_addressid').val(uniqId("ADDR_"));
        }
        $('#'+id_prefix+'_google_place_id').val(place.place_id);
        $('#'+id_prefix+'_google_latitude').val(place.geometry.location.lat());
        $('#'+id_prefix+'_google_longitude').val(place.geometry.location.lng());

        var address_components = place.address_components;
        place.address_components.forEach(function(address_component) {
            var type = address_component.types[0];
            var short_name = address_component.short_name;
            if (type === "street_number") {
                console.log("Street number: " + short_name);
                $('#'+id_prefix+'_streetnumber').val(short_name);
            } else if (type === "route") {
                console.log("Street name: " + short_name);
                $('#'+id_prefix+'_streetname').val(short_name);
            } else if (type === "neighborhood") {
                console.log("Neighborhood: " + short_name);
            } else if (type === "locality") {
                console.log("City: " + short_name);
                $('#'+id_prefix+'_city').val(short_name);
            } else if (type === "administrative_area_level_2") {
                console.log("County: " + short_name);
            } else if (type === "administrative_area_level_1") {
                console.log("State: " + short_name);
                $('#'+id_prefix+'_state').val(short_name);
            } else if (type === "postal_code") {
                console.log("Zipcode: " + short_name);
                $('#'+id_prefix+'_zipcode').val(short_name);
            } else if (type === "postal_code_suffix") {
                console.log("Zip Suffix: " + short_name);
            } else {
                console.log("address_component.short_name: " + short_name);
            }
        });
        markAddressOnMap(id_prefix+"_google_map", place.formatted_address);
    });
}

function markAddressOnMap(element_id, address) {
    var map = new google.maps.Map(document.getElementById(element_id), {
        zoom: 4,
        center: {lat: 39.82, lng: -98.57}
    });
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({'address': address}, function(results, status) {
        if (status === 'OK') {
            map.setCenter(results[0].geometry.location);
            map.setZoom(16);
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location,
                label: 'A'
            });
        } else {
            console.log('Geocode was not successful for the following reason: ' + status);
        }
    });
}

function uniqId(prefix) {
    if (window.performance) {
        var s = performance.timing.navigationStart;
        var n = performance.now();
        var base = Math.floor((s + Math.floor(n))/1000);
    } else {
        var n = new Date().getTime();
        var base = Math.floor(n/1000);
    }
    var ext = Math.floor(n%1000*1000);
    var now = ("00000000"+base.toString(16)).slice(-8)+("000000"+ext.toString(16)).slice(-5);
    if (now <= window.my_las_uid) {
        now = (parseInt(window.my_las_uid?window.my_las_uid:now, 16)+1).toString(16);
    }
    window.my_las_uid = now;
    return (prefix?prefix:'')+now;
}
