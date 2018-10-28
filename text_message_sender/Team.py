from send_message import send_message as send
import re

class Team:
    """
    Creates a Team with the parameters team_id, team_name, coah_name, students_names, phone_numbers.
    @param team_id: unique id of team
    @param team_name: name of the team
    @param coach_name: name of the team coach
    @param students_names: list of names of students in the team
    @param phone_numbers: list of phone numbers
    """
    def __init__(self, team_id, team_name, coach_name, students_names, phone_numbers):
        self.team_id = team_id
        self.team_name = team_name
        self.coach_name = coach_name
        self.students_names = students_names
        self.phone_numbers = phone_numbers

    def set_team_id(self, team_id):
        # set the team_id as team_id
        self.team_id = team_id

    def set_team_name(self, team_name):
        # set the team_name as team_name
        self.team_name = team_name

    def set_coach_name(self, coach_name):
        # set the coach_name as coach_name
        self.coach_name = coach_name

    def set_students_names(self, students_names):
        # set the students_names as students_names
        self.students_names = students_names

    def set_phone_numbers(self, phone_numbers):
        # set the phone_numbers as phone_numbers
        self.phone_numbers = phone_numbers

    def get_team_id(self):
        # returns the team_id
        return self.team_id

    def get_team_name(self):
        # returns the team_name
        return self.team_name

    def get_coach_name(self):
        # returns the coach_name
        return self.coach_name

    def get_students_names(self):
        # returns the students_names
        return self.students_names

    def get_phone_numbers(self):
        # returns the phone_numbers
        return self.phone_numbers

    #replace {{team_id}}/{{teamid}}, {{team_name}}/{{teamname}}, {{coach_name}}/{{coachname}}/{{coach}}, {{all_students}} with respective values
    def send_message(self, message):
        """
        Formats the students_names in students_format,
        creates a key-value pair dictionary cpatterns
        with the values as team_id, team_name, coach_name,
        and the students_format. Then substitutes in all
        values found in patterns and sends a message to
        all members of a team.
        """
        students_format = ""
        for i in range(len(self.students_names)-1):
            students_format += self.students_names[i] + ", "
        students_format += self.students_names[-1]
        patterns = {"{{team_?id}}": self.team_id, "{{team_?name}}": self.team_name, "{{coach_?n?a?m?e?}}": self.coach_name, "{{all_students}}": students_format}
        for item in patterns.items():
            message = re.sub(item[0], item[1], message)
        for phone_number in self.phone_numbers:
            send(message, phone_number)

