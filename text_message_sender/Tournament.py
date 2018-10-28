import pandas as pd
import re
from Team import Team
class Tournament:
    def __init__(self, path):
        self.info = pd.read_csv(path)
        self.teams = {}
        self.students = {}
        for row in info.index:
            tm = extract_team_info(info, row)
            teams[tm.get_team_id] = tm
            for student in tm.get_students_names:
                students[student.get_student_id] = student
    def extract_team_info(pd, team):
        students_names = [pd.loc[team, '\StudentA'], 
                         pd.loc[team, '\StudentB'], 
                         pd.loc[team, '\StudentC'], 
                         pd.loc[team, '\StudentD'], 
                         pd.loc[team, '\StudentE']]
        team_info = {"team_id": pd.loc[team, '\TeamID'],
                    "team_name": pd.loc[team, '\TeamName'], 
                    "coach_name": pd.loc[team, '\CoachName'], 
                    "students_names": students_names, 
                    "phone_numbers": pd.loc[team, '\PhoneNumbers']}
        return Team(team_info)
    def send_general_message(message):
        for team in self.team:
            team.send_message(message)
    def send_targeted_message(message, lst_student_id):
        grouped_by_teams = {}
        for student_id in lst_student_id:
            student = students[student_id]
            team = student.get_team()
            if team in grouped_by_teams:
                grouped_by_teams[team] += " " + student.get_student_name() + ","
            eles:
                grouped_by_teams[team] = [student] + ","
        for team in grouped_by_teams:
            team.send_message(re.sub("{targed_students}", grouped_by_teams[team], message))
