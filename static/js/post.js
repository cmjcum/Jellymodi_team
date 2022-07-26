function show_image(obj) {
    let url = URL.createObjectURL(event.target.files[0]);

    let siblings = $(obj).siblings();
    siblings.hide();

    let parent = $(obj).parent();
    if ($(obj).attr('id') == 'face_img') {
        let face_img = $('#face_img')[0].files[0];

        let form_data = new FormData();
        form_data.append('face_img', face_img);

        $.ajax({
            type: 'POST',
            url: '/post/change',
            data: form_data,
            cache: false,
            contentType: false,
            processData: false,
            success: function (response) {
                parent.css({
                    'background-image': `url(${response['url']}`,
                    'background-size': 'cover',
                    'border-radius': '0',
                    'box-shadow': 'none'
                });
            },
            error: function (response) {
                alert('error')
            }
        });
    } else {
        parent.css({'background-image': `url(${url}`, 'background-size': 'cover', 'border': 'none'});
    }
}

function submit() {
    let desc = $('#desc').val();
    let additional_img = $('#additional_img')[0].files[0];

    let form_data = new FormData();
    form_data.append('desc', desc);
    if(additional_img != undefined)
        form_data.append('additional_img', additional_img);

    $.ajax({
        type: 'POST',
        url: "/post/upload",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            window.location.href = '/'
        }
    });
}

