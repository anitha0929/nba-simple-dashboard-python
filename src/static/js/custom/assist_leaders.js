$(function() {
    function get_columns(data) {
        var columns = [];

        if (data.length > 0) {
            var columnsIn = data[0];
            for (var key in columnsIn) {
                columns.push({
                    field: key,
                    title: key
                })
            }
        } else {
            console.log("No columns");
        }
        return columns;

    };

    function populate_data(data){
            var leaders = JSON.parse(data.leaders);
            var leader = data.leader;
            var pct = data.pct;
            var leaderTxt = leader + ' is the Assist Leader with ' + pct + ' FGM';
            document.getElementById("leader").innerHTML = leaderTxt;
            $("#table_leaders").bootstrapTable({
                data: leaders,
                columns: get_columns(leaders)
            });
    }

$( document ).ready(function() {
    $("#info").show();
     $.getJSON('/get_assist_leaders', {
        }, function(data) {
            var alert_msg = ''
            $("#info").hide();
            if (data.error) {
                alert_msg = data.error;
                $("#error-info").text(alert_msg);
                $("#error-info").show();
            } else {
                populate_data(data);
            }
        });

});

});