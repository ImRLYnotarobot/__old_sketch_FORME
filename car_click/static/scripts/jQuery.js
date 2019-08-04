$(document).ready(function () {

    var model_specs,
        model_price,
        model_cur_price,
        specs_holder,
        price_holder;

    specs_holder = $('#modelSpecs');
    price_holder = $('#modelPrice');
    cur_price_holder = $('#modelCurPrice');
    cur_message_holder = $('#cur_message');

    model_price = 0;
    model_cur_price = 0;
    model_specs = '';


    my_mlg_api_url = 'http://localhost:8000/api/coef_from_rur/';
    target_cur = 'usd';
    // price_ratio = get_ratio(target_cur);
    // alert(price_ratio);


    function calc_price() {
        model_price = parseInt($('input[name=engine]:checked', '#config_form').val());
        model_price += parseInt($('input[name=gear]:checked', '#config_form').val());
        model_price += parseInt($('input[name=pack]:checked', '#config_form').val());
    }


    function add_space(n_str) {
        n_str += '';
        x = n_str.split('.');

        x1 = x[0];
        x2 = x.length > 1 ? '.' + x[1] : '';
        var rgx = /(\d+)(\d{3})/;
        while (rgx.test(x1)) {
            x1 = x1.replace(rgx, '$1' + ' ' + '$2');
        }
        return x1 + x2;
    }


    function compile_specs() {
        model_specs = $('input[name=engine]:checked + label', '#config_form').text();
        model_specs += ', ' + $('input[name=gear]:checked + label', '#config_form').text();
        model_specs += ', ' + $('input[name=pack]:checked + label', '#config_form').text();
    }

    function fill_cur_price_field() {
        if (!ratio) {
            cur_message_holder.text('неправильный код')
        } else {
            model_cur_price = parseInt(model_price * ratio);
            cur_price_holder.text(add_space(model_cur_price) + ' ' + target_cur.toUpperCase());
        }
    }

    function fill_fields() {
        calc_price();
        compile_specs();
        price_holder.text(add_space(model_price) + ' Руб.');
        specs_holder.text(model_specs);
    }

    function get_ratio(t_cur) {
        $.ajax({
            url: my_mlg_api_url,
            type: 'get',
            data: {
                'target_cur': t_cur
            },
            cache: false,
            success: function (json_str) {
                ratio = parseFloat(json_str.ratio);
                // console.log(ratio);
                fill_cur_price_field();
            }
        });

    }

    $('.cur_toggle').on('click', function () {
        $('.cur_dropdown').slideToggle('fast');
    });

    $('#cur_submit').on('click', function () {
        target_cur = $('#target_cur').val();
        cur_message_holder.text('');
        get_ratio(target_cur);
    });

    $('#config_form input').on('change', function () {
        fill_fields();
        fill_cur_price_field();
    });


    $('.color_select .color_item').on('click', function () {
        $(this).addClass('selected');
        $(this).siblings('.color_item').removeClass('selected');
        var pic_path = $(this).attr('data-img');
        $('#imgHolder img').attr('src', pic_path);
    });


    $('.color_item').on('mouseenter', function () {
        $(this).toggleClass('focused');
    });


    $('.color_item').on('mouseleave', function () {
        $(this).toggleClass('focused');
    });


    // calc_price();
    // compile_specs();
    fill_fields();
    get_ratio(target_cur);

});