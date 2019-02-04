$('.dropdown-toggle').dropdown();

$().button('toggle');

$('.plus-btn').on('click', function() {
    var $input = $(this).closest('div').find('input');
    var $value = parseInt($input.val());

    $value = $value + 1;    

    $input.val($value);
})

$('.minus-btn').on('click', function() {
    var $input = $(this).closest('div').find('input');
    var $value = parseInt($input.val());

 
    if ($value > 1) {
        $value = $value - 1;
    } else {
        $value = 0;
    }

    $input.val($value);
})