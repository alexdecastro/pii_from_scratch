$(document).ready(function() {
    var table = $('#data_table_02').DataTable({
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
