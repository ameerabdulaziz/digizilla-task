function loginValidation(event) {
    event.preventDefault();
    const form = $('#login_form');
    const urlValidator = form.attr('data-url-validator');
    const urlSuccess = form.attr('data-url-success');
    const csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
    const username = $('#id_username').val();
    const password = $('#id_password').val();
    $.ajax({
        method: 'POST',
        url: urlValidator,
        data: {
            csrfmiddlewaretoken,
            username,
            password
        },
        success: (data) => {
            if (data.valid) {
                window.location.replace(urlSuccess);
            } else {
                $('#id_username').addClass('is-invalid');
                $('#id_password').val('').addClass('is-invalid');
                $('#error').html(data.error).css('display', 'block');
            }
        }, error: (error) => {
            console.log('error')
        }
    })
}