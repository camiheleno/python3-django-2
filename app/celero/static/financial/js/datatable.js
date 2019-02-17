$(document).ready(function() {
    var dt_table = $('.datatable').dataTable({
        "oLanguage": oLanguages,
        "bFilter": true,
        "aLengthMenu": [[25, 50, 100, 200], [25, 50, 100, 200]],
        "iDisplayLength" : 25,
        "aaSorting": [[ 0, "desc" ]],
        "bAutoWidth": true,
        "aoColumns": [
            { "bSortable": true, "sClass": "center" },
            { "bSortable": false, "sClass": "center" },
            { "bSortable": true, "sClass": "center" },
            { "bSortable": false, "sClass": "center" },
        ],
        "bProcessing": true,
        "bServerSide": true,
        "bStateSave": true,
        "searching": false,
        "bFilter": false,
        "sAjaxSource": USERS_LIST_JSON_URL
    });
});