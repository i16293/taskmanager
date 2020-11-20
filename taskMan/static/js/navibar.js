$(function($) {
    WindowHeight = $(window).height()

    $(document).ready(function() {
        $('.barbtn').click(function(){
            if($('.drawr').is(":animated")){
                return false;
            }else{
                $('.drawr').animate({width:'toggle'});
                $(this).toggleClass('peke');
                return false;
            }
        });
    });

    //別領域をクリックでメニューを閉じる
    $(document).click(function(event) {
        if (!$(event.target).closest('.drawr').length) {
            $('.barbtn').removeClass('peke');
            $('.drawr').hide();
        }
    });

});