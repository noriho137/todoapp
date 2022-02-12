function do_update() {
    console.log('do_update');
    event.preventDefault();

    var value = $(this).attr('value');
    var action = '/task/' + value + '/update/';
    var method = 'post';
    var form = $(this).parents('form');
    do_update_ajax(action, method, form.serialize());
}

$('button[name="update"]').on('click', do_update);

$(function () {
    $("#datetimepicker_update").datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss',
    });
});
