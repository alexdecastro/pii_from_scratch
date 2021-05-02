
var pguid = document.getElementById("id_pguid").value;


$(document).ready(function() {


    $("#EventLogs").on('click',function() {


          var url = '/pii/participants/participant-events' + "/" + pguid;

          location.href = url;
    });

    $('#NewAddress').on('click', function (e) {

        alert ('Click works');

        if (pguid == '') {
            alert ('Please select one participoant from the table');
        } else {
            var url = 'participant-view' + "/" + pguid;
            // Construct the full URL with "id" + "/" + id;
            location.href = url;
        }
    });


       $('#EditParticipant').on('click', function (e) {

        if (pguid == '') {
            alert ('Please select one participoant from the table');
        } else {
            var url = '/pii/participants/participant-view' + "/" + pguid;
            // Construct the full URL with "id" + "/" + id;
            location.href = url;
        }
    });


    $('#Locator').on('click', function (e) {

        if (pguid == '') {
            alert ('Please select one participoant from the table');
        } else {
            var url = '/pii/participants/locator' + "/" + pguid;
            // Construct the full URL with "id" + "/" + id;
            location.href = url;
        }
    });




    $('#Residential').on('click', function (e) {

        if (pguid == '') {
            alert ('Please select one participant from the table');
        } else {
            var url = '/pii/residentialinfo3' + "/" + pguid;
            // Construct the full URL with "id" + "/" + id;
            location.href = url;
        }
    });

    $('#Informant').on('click', function (e) {

        if (pguid == '') {
            alert ('Please select one participant from the table');
        } else {
            var url = '/pii/participants/informant' + "/" + pguid;
            // Construct the full URL with "id" + "/" + id;
            //location.href = url;
            alert ('Open informant page ');

        }
    });

    $('#School').on('click', function (e) {

        if (pguid == '') {
            alert ('Please select one participant from the table');
        } else {
            var url = '/pii/participants_schools' + "/" + pguid;
            // Construct the full URL with "id" + "/" + id;
            location.href = url;
        }
    });


    $('#OpenRedcap').on('click', function (e) {

        if (pguid == '') {
            alert ('Please select one participoant from the table');
        } else {
            var url = 'https://ip66.ucsd.edu/redcap/redcap_v10.0.0/DataEntry/index.php?pid=12&id=' + pguid + '&event_id=50&page=special_instrument_participation';
            // Construct the full URL with "id" + "/" + id;
            location.href = url;
        }
    });

     $('#OpenSchedule').on('click', function (e) {

        if (pguid == '') {
            alert ('Please select one participoant from the table');
        } else {
            var url = 'https://ip66.ucsd.edu/redcap/redcap_v10.0.0/DataEntry/index.php?pid=12&id=' + pguid + '&event_id=50&page=scheduled';
            // Construct the full URL with "id" + "/" + id;
            location.href = url;
        }
    });

    $('#OpenMilliSecond').on('click', function (e) {

        if (pguid == '') {
            alert ('Please select one participoant from the table');
        } else {
            // var url = 'https://ip66.ucsd.edu/redcap/redcap_v10.0.0/DataEntry/index.php?pid=12&id=' + pguid + '&event_id=50&page=scheduled';
            // Construct the full URL with "id" + "/" + id;
            // location.href = url;
            alert ('Open Millisecond page ');
        }
    });

    $('#OpenKSADS').on('click', function (e) {

        if (pguid == '') {
            alert ('Please select one participoant from the table');
        } else {
            alert ('Open KSADS page ');
        }
    });

})

