function show_update() {
    console.log('show_update');
    var value = $(this).attr('value');
    var action = '/task/' + value + '/update/';
    var method = 'get';
    show_update_ajax(action, method);
}

function show_delete() {
    console.log('show_delete');
    var value = $(this).attr('value');
    var action = '/task/' + value + '/delete/';
    var method = 'get';
    show_delete_ajax(action, method);
}

$('button[name="edit"]').on('click', show_update);
$('button[name="delete"]').on('click', show_delete);
