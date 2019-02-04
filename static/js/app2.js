$('.dropdown-toggle').dropdown()
$().button('toggle')

$('.btn-number').click(function(e){
    e.preventDefault();

$('.minus-btn').on('click', function(e) {
    e.preventDefault();
    var $this = $(this);
    var $input = document.getElementbyId('child_count');
    var value = parseInt($input.val());
 
    if (value &amp;gt; 1) {
        value = value - 1;
    } else {
        value = 0;
    }
 
  $input.val(value);
 
});
 
$('.plus-btn').on('click', function(e) {
    e.preventDefault();
    var $this = $(this);
    var $input = document.getElementbyId('child_count');
    var value = parseInt($input.val());
 
    if (value &amp;lt; 100) {
        value = value + 1;
    } else {
        value =100;
    }
 
    $input.val(value);
});
    