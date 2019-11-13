$(document).ready(function () {
    $('#root-form').submit(function (e) {

        $('.invalid-feedback').remove();
        $('input').removeClass('is-invalid');
        $('textarea').removeClass('is-invalid');

        let email = $('#Email1')
        let school = $('#School1')
        let ratingParagraph = $('#Experience2')
        let improvements = $('#Improve1')
        let validity = true;

        if (email.val().length < 1) {
            email.addClass("is-invalid");
            email.after('<div class="invalid-feedback">Please enter an email</div>');
            validity = false;
        }

        if (school.val().length < 1) {
            school.addClass("is-invalid");
            school.after('<div class="invalid-feedback">Please enter a school.</div>');
            validity = false;
        }

        if (ratingParagraph.val().length < 1) {
            ratingParagraph.addClass("is-invalid");
            ratingParagraph.after(
                '<div class="invalid-feedback">Please explain why you chose that rating.</div>'
            );
            validity = false;
        }

        if (improvements.val().length < 1) {
            improvements.addClass("is-invalid")
            improvements.after(
                '<div class="invalid-feedback">Please let us know how we could improve.</div>'
            );
            validity = false;
        }


        if (validity === true) {
            $('#root-form').submit();
        } else if (validity !== true) {
            e.preventDefault();
        }

    });
});