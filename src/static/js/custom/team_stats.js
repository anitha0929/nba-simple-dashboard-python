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

    function populate_data(data,id){
            var team_stats = JSON.parse(data.team_stats);
            var table_id = '#' + 'table_division_stats' + '_' + id;
            console.log(table_id);

            $(table_id).bootstrapTable({
                data: team_stats,
                columns: get_columns(team_stats)
            });
    }

    $('a.division').bind('click', function() {

        var id = this.id;
        $("#info").show();
        $.getJSON('/team-standing-by-division', {
            division: this.id,
        }, function(data) {

            var alert_msg = ''
            $("#info").hide();
            if (data.error) {
                alert_msg = data.error;
                $("#error-info").text(alert_msg);
                $("#error-info").show();
            } else {
                populate_data(data, id);
            }
        });
        return false;
    });

});