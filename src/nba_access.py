import nba_py
import nba_py.team
import nba_py.league
from marshmallow import fields, Schema
import pandas as pd

class NBA_Access():

    def __init__(self, division=''):
     self.division = division

    def get_stats_by_division(self):
        """
given a division, returns stats for that division from nab_py for the current season
        :return:
        """
        team_stats = nba_py.league.TeamStats(division=self.division)
        print(team_stats)
        return team_stats.overall()

    def get_team_stats_schema(self):
        schema = Teams_schema(many=True)
        team_stats = self.get_stats_by_division()
        team_stats_dict = team_stats.to_dict(orient='records')
        team_stats_schema = schema.dumps(team_stats_dict)
        return team_stats_schema

    def get_leaders(self):
        """
retuns the leading point scorers from nba_py
        :return:
        """
        leaders = nba_py.league.Leaders()
        result_df = leaders.results()
        filtered_result_df = result_df.filter(items=['PLAYER', 'TEAM','PTS'])
        filtered_result_df = filtered_result_df.sort_values(by=['PTS'],ascending=False)
        head_filtered_result_df = filtered_result_df.head(20)
        return head_filtered_result_df

    def get_leaders_schema(self):
        schema = Leaders_schema(many=True)
        leaders = self.get_leaders()
        leaders_dict = leaders.to_dict(orient='records')
        leaders_schema = schema.dumps(leaders_dict)
        return [leaders_schema, leaders.iloc[0]['PLAYER'], leaders.iloc[0]['PTS']]

    def get_assist_leaders(self):
        """
Fetches the Assist details from nba_py, finds the top assist and returns the top 20
        :return:
        """
        columns = ['PLAYER_NAME', 'PLAYER_ID', 'FGM', 'TEAM_NAME', 'TEAM_CITY']
        assist_df = pd.DataFrame(columns=columns)
        teams = nba_py.constants.TEAMS
        for key, val in teams.items():
            team_id = val['id']
            team_name = val['name']
            team_city = val['city']
            assist_obj = nba_py.team.TeamShootingSplits(team_id=team_id)
            response_df = assist_obj.assisted_by()
            response_df.assign(team_name=team_name, team_city=team_city)
            temp_df = response_df.filter(['PLAYER_NAME', 'PLAYER_ID', 'FGM'])
            temp_df['TEAM_NAME'] = team_name
            temp_df['TEAM_CITY'] = team_city
            assist_df = assist_df.append(temp_df, ignore_index=True)
            break

        assist_df = assist_df.sort_values(by=['FGM'], ascending=False)
        return (assist_df.head(20))

    def get_assist_leaders_schema(self):
        schema = Assist_leaders_schema(many=True)
        assist_leaders = self.get_assist_leaders()
        assist_leaders_dict = assist_leaders.to_dict(orient='records')
        assist_leaders_schema = schema.dumps(assist_leaders_dict)
        return [assist_leaders_schema, assist_leaders.iloc[0]['PLAYER_NAME'], assist_leaders.iloc[0]['FGM']]


# The schema classes identifies the fields to be returns

class Teams_schema(Schema):
    class Meta:
        ordered = True
    TEAM_NAME = fields.String()
    L = fields.String()
    W = fields.String()
    W_PCT = fields.String()
    W_RANK = fields.String()
    GP = fields.String()

class Leaders_schema(Schema):
    class Meta:
        ordered = True
    PLAYER = fields.String()
    TEAM = fields.String()
    PTS = fields.String()

class Assist_leaders_schema(Schema):
    class Meta:
        ordered = True
    PLAYER_NAME = fields.String()
    FGM = fields.String()
    TEAM_NAME = fields.String()
    TEAM_CITY = fields.String()