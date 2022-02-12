function show_detail() {
    console.log('show_detail');
    var data_action = $(this).attr('data-action');
    var data_method = $(this).attr('data-method');
    show_detail_ajax(data_action, data_method);
}

$('button[name="todo"]').on('click', show_detail);
$('button[name="doing"]').on('click', show_detail);
$('button[name="done"]').on('click', show_detail);

$(function () {
    $("#datetimepicker_home").datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss',
    });
});
