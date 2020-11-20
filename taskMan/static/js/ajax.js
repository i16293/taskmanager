// プロジェクトタスク追加Ajax
$(function () {
    $('#TaskAddAjax').click(function () {

        //必須事項チェック
        let taskName = $('input[name=taskName]').val();

        if (taskName != "") { //入力があるかどうかないならELSE

            var $form = $('form[name=addTask]');
            //送信
            $.ajax({
                url: $form.prop("action"),
                method: $form.prop("method"),
                data: $form.serialize(),
                dataType: "JSON",
            })
                .done(function (data) {
                    var result = JSON.parse(data['taskdata'])

                    $('#taskAccordion').empty()

                    $.each(result, function (k, v) {
                        let taskData = v["fields"]

                        let taskHtml = '<li class="task' + taskData["priolity"] + '">' + taskData["task_name"] + '</li>'

                        $('#taskAccordion').append(taskHtml)
                    })
                })

        } else {
            alert('タスク名を入力してください')

    })
})