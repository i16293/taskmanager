// メンバー削除チェックボックス表示
$(function () {
    $('.MDC').hide();

    $('.MDB').click(function () {
        $('.MD').hide();
        $('.MDC').show();
    })
})

// メンバー削除チェックボックス非表示
$(function () {
    $('.MDCB').click(function () {
        $('.CCB').prop('checked', false);
        $('.CPB').css('visibility', 'hidden');
        $('.MDC').hide();
        $('.MD').show();
    })
})

// チェックボックスが選択されている場合のみボタンが活性状態になる
$(function() {
    $('.CPB').css('visibility', 'hidden');

    $('.CCB').change(function () {
        if ($('.CCB:checked').length == 0) {
            $('.CPB').css('visibility', 'hidden');
        } else {
            $('.CPB').css('visibility', 'visible');
        }
    })
})