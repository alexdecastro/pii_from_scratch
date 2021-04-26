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
    var data_table_01 = $('#data_table_01').DataTable({ // page 10 entries at a time
        filter: true, // enable search field
        "order": [[ 6, "desc" ]] // sort by column 6 descending Yes then No
    });
});
