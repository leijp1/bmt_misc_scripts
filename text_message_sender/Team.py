from send_message import send_message as send
import re

class Team:
    def __init__(self, team_id, team_name, coach_name, students_names, phone_numbers):
        self.team_id = team_id
        self.team_name = team_name
        self.coach_name = coach_name
        self.students_names = students_names
        self.phone_numbers = phone_numbers

    def set_team_id(self, team_id):
        self.team_id = team_id

    def set_team_name(self, team_name):
        self.team_name = team_name

    def set_coach_name(self, coach_name):
        self.coach_name = coach_name

    def set_students_names(self, students_names):
        self.students_names = students_names

    def set_phone_numbers(self, phone_numbers):
        self.phone_numbers = phone_numbers

    def get_team_id(self):
        return self.team_id

    def get_team_name(self):
        return self.team_name

    def get_coach_name(self):
        return self.coach_name

    def get_students_names(self):
        return self.students_names

    def get_phone_numbers(self):
        return self.phone_numbers

    #replace {{team_id}}/{{teamid}}, {{team_name}}/{{teamname}}, {{coach_name}}/{{coachname}}/{{coach}}, {{all_students}} with respective values
    def send_message(self, message):
        students_format = ""
        for i in range(len(self.students_names)-1):
            students_format += self.students_names[i] + ", "
        students_format += self.students_names[-1]
        patterns = {"{{team_?id}}": self.team_id, "{{team_?name}}": self.team_name, "{{coach_?n?a?m?e?}}": self.coach_name, "{{all_students}}": students_format}
        for item in patterns.items():
            message = re.sub(item[0], item[1], message)
        for phone_number in self.phone_numbers:
            send(message, phone_number)

