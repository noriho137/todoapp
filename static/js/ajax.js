function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        }
    }
});

function show_detail_ajax(url, method) {
    console.log('show_detail_ajax');
    $.ajax({
        url: url,
        method: method,
        timeout: 10000,
        dataType: 'html',
    }).done(function(response) {
        console.log('done');
        // TODO: html()はDOM-based XSSの恐れあり
        $('#myModal1').html(response);
        $('#detailModal').modal('show');
    }).fail(function(jqXHR, textStatus, errorThrown) {
        console.log('fail');
        console.log(jqXHR.status);
        console.log(textStatus);
        console.log(errorThrown);
        alert(jqXHR.status + ' Error: ' + errorThrown);
    }).always(function() {
        console.log('always');
    });
}

function show_update_ajax(url, method) {
    console.log('show_update_ajax');
    $.ajax({
        url: url,
        method: method,
        timeout: 10000,
        dataType: 'html',
    }).done(function(response) {
        console.log('done');
        // TODO: html()はDOM-based XSSの恐れあり
        $('#myModal2').html(response);
        $('#updateModal').modal('show');
    }).fail(function(jqXHR, textStatus, errorThrown) {
        console.log('fail');
        console.log(jqXHR.status);
        console.log(textStatus);
        console.log(errorThrown);
        alert(jqXHR.status + ' Error: ' + errorThrown);
    }).always(function() {
        console.log('always');
    });
}

function do_update_ajax(url, method, data) {
    console.log('do_update_ajax');
    console.log(url, method);
    $.ajax({
        url: url,
        method: method,
        data: data,
        timeout: 10000,
        dataType: 'html',
    }).done(function(response) {
        console.log('done');
        $('#updateModal').modal('hide');
        // 詳細表示モーダルの中身を書き換える
        // TODO: html()はDOM-based XSSの恐れあり
        $('#detailModal .modal-body').html(response);
    }).fail(function(jqXHR, textStatus, errorThrown) {
        console.log('fail');
        console.log(jqXHR.status);
        console.log(textStatus);
        console.log(errorThrown);
        alert(jqXHR.status + ' Error: ' + errorThrown);
    }).always(function() {
        console.log('always');
    });
}

function show_delete_ajax(url, method) {
    console.log('show_delete_ajax');
    $.ajax({
        url: url,
        method: method,
        timeout: 10000,
        dataType: 'html'
    }).done(function(response) {
        console.log('done');
        // TODO: html()はDOM-based XSSの恐れあり
        $('#myModal3').html(response);
        $('#deleteModal').modal('show');
    }).fail(function(jqXHR, textStatus, errorThrown) {
        console.log('fail');
        console.log(jqXHR.status);
        console.log(textStatus);
        console.log(errorThrown);
        alert(jqXHR.status + ' Error: ' + errorThrown);
    }).always(function() {
        console.log('always');
    });
}

//function delete_task_ajax(url, method, data) {
//    console.log('delete_task_ajax');
//    console.log(url, method);
//    $.ajax({
//        url: url,
//        method: method,
//        data: data,
//        timeout: 10000,
//    }).done(function(response) {
//        console.log('done');
//        $('#deleteModal').modal('hide');
//        $('#detailModal').modal('hide');
//        window.location.reload();
//    }).fail(function(jqXHR, textStatus, errorThrown) {
//        console.log('fail');
//        console.log(jqXHR.status);
//        console.log(textStatus);
//        console.log(errorThrown);
//        alert(jqXHR.status + ' Error: ' + errorThrown);
//    }).always(function() {
//        console.log('always');
//    });
//}
