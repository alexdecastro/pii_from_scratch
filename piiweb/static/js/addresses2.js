function handleButtonClick(element) {
    console.log("handleButtonClick");
    var addr_id = $(element).attr('id');
    var button_text = $(element).text();
    console.log("pguid: "+pguid+" addr_id: " + addr_id + " button_text: " + button_text);
    if (button_text === "Edit") {
        edit_address(addr_id);
    }
}

function edit_address(addr_id) {
    alert("edit_address: addr_id: " + addr_id);
}

function create_part_addr(pguid, addr_id) {
        $.ajax({
            type: "POST",
            url: "/piiweb/addresses/create_part_addr/"+pguid+"/"+addr_id+"/",
            success: function (response) {
                console.log(response);
            }
        });
}

function delete_part_addr(pguid, addr_id) {
        $.ajax({
            type: "POST",
            url: "/piiweb/addresses/delete_part_addr/"+pguid+"/"+addr_id+"/",
            success: function (response) {
                console.log(response);
            }
        });
}

$(document).ready(function() {
    var data_table_01 = $('#data_table_01').DataTable({ // page 10 entries at a time
        filter: true, // enable search field
        "order": [[ 8, "desc" ]] // sort by column 6 descending Yes then No
    });
});