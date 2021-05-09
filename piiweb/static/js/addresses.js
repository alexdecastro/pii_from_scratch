function handleButtonClick(element) {
    console.log("handleButtonClick");
    var button_type = $(element).data('type');
    console.log("handleButtonClick: button_type: " + button_type);
    if (button_type.includes('show')) {
        var address = $(element).data('address');
        console.log("address: " + address);
        // show address on map
    } else if (button_type.includes('edit')) {
        var addr_id = $(element).attr('id');
        console.log("addr_id: " + addr_id);
        edit_address(addr_id);
    } else {
        // do nothing
    }

}

function edit_address(addr_id) {
    var url = '/pii/addresses/address-view' + "/" + addr_id;
    location.href = url;
}

$(document).ready(function() {
    var data_table_01 = $('#data_table_01').DataTable({ // page 10 entries at a time
        filter: true, // enable search field
        "order": [[ 2, "asc" ]] // sort by street name
    });

    $('#id_new_address').on('click', function (e) {
        var url = '/pii/addresses/address-new';
        location.href = url;
    });
});
