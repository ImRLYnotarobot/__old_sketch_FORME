$(document).ready(function () {

    $dyn_image = $('.image_class');

    $('#colorSelector .colorItem').on('click', function () {
        var image_path;
        var time_delay = 100;
        image_path = $(this).attr('data-img-path');
        // alert(image_path);
        $dyn_image.fadeOut(time_delay, function () {
            $dyn_image.attr('src', image_path).fadeIn(time_delay);
        });
    });
});