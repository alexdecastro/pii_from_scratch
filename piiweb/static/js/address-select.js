function handleButtonClick(element) {
    console.log("handleButtonClick");
    var addr_id = $(element).attr('id');
    var button_text = $(element).text();
    console.log("pguid: "+pguid+" addr_id: " + addr_id + " button_text: " + button_text);
    if (button_text === "Yes") {
        $(element).text("No");
        $(element).removeClass('btn-success');
        $(element).addClass('btn-danger');
    } else {
        $(element).text("Yes");
        $(element).removeClass('btn-danger');
        $(element).addClass('btn-success');
    }
}

$(document).ready(function() {
    var table = $('#datatables').DataTable({
        filter: true,
        "order": [[ 6, "desc" ]]
    });

    var table = $('#datatablesXXX').DataTable({
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]], // 10 rows
        "responsive": true,
        "scrollY": true,
        "scrollX": true,
        "processing": true,
        "serverSide": true,

        "ajax": {
            "url": "/api/addresses/",
            "type": "GET"
        },
        "columns": [
            {
                "className": 'details-control',
                "orderable": false,
                "data": null,
                "defaultContent": ''
            },
            {"data": "addressid"},
            {"data": "streetnumber"},
            {"data": "streetname"},
            {"data": "aptnumber"},
            {"data": "nearest"},
            {"data": "city"},
            {"data": "state"},
            {"data": "zipcode"},
            {"data": "google_place_id"},
            {
                "className": "editbutton",
                "data": null,
                "defaultContent": '<button type="button" class="btn btn-info">Edit</button>'
            }
        ]
    });
});
