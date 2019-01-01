from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

DASHBOARD_DICT = {'Team standings By Division': '/team-standings/', 'Leading Point Scorer over all divisions': '/leading-point-scorers/','Assist Leader over all divisions': '/assist_leaders/'}


@app.route('/')
def dashboard():
    """
This route renders the initial welcome page
    :return:
    """
    return render_template("index.html", DASHBOARD_DICT=DASHBOARD_DICT)


@app.route('/team-standings/')
def team_standings():
    """
This route renders the html that fetches and displays the team stats view
    :return:
    """
    try:
        return render_template("team_stats.html")

    except Exception as e:
        return str(e)


@app.route('/leading-point-scorers/')
def leaders_pts():
    """
This function renders the html to view the leading point scorers
    :return:
    """
    try:
        return render_template("leaders.html")

    except Exception as e:
        return str(e)


@app.route('/get_leaders/')
def leaders():
    """
This function return the leading point scorer as api response for the current season
    :return:
    """
    try:
        from nba_access import NBA_Access

        nbaaccess_obj = NBA_Access()
        leaders_schema_array = nbaaccess_obj.get_leaders_schema()
        leaders_schema = leaders_schema_array[0]
        return jsonify({'leaders': leaders_schema.data, 'leader': leaders_schema_array[1], 'pct':leaders_schema_array[2]})
    except Exception as e:
        return str(e)


@app.route('/assist_leaders/')
def assist_leaders():
    """
This functions renders the assist leaders htmls page that displays the Assist leaders details
    :return:
    """
    try:
        return render_template("assist_leaders.html")

    except Exception as e:
        return str(e)


@app.route('/get_assist_leaders/')
def get_assist_leaders():
    """
returns tops 20 assit leaders in the api response for the current season
    :return:
    """
    try:
        from nba_access import NBA_Access

        nbaaccess_obj = NBA_Access()
        leaders_schema_array = nbaaccess_obj.get_assist_leaders_schema()
        leaders_schema = leaders_schema_array[0]
        return jsonify({'leaders': leaders_schema.data, 'leader': leaders_schema_array[1], 'pct':leaders_schema_array[2]})
    except Exception as e:
        return str(e)


@app.route('/team-standing-by-division/')
def team_standing_by_division():
    """
This route handles the jquery call to view the stats for a given division
    :return:
    """
    try:
        from nba_access import NBA_Access

        division_current = request.args.get('division', 0, type=str)
        nbaaccess_obj = NBA_Access(division=division_current)
        team_stats_schema = nbaaccess_obj.get_team_stats_schema()

        return jsonify({'team_stats': team_stats_schema.data})

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)






