from .text-message-sender import send-message


class Team:
    def __init__(self, team_id, team_name, coach_name, students_names, phone_numbers):
        self.team_id = team_id
        self.team_name = team_name
        self.coach_name = coach_name
        self.students_names = students_names
        self.phone_numbers = phone_numbers

    def set_team_id(team_id):
        self.team_id = team_id

    def set_team_name(team_name):
        self.team_name = team_name

    def set_coach_name(coach_name):
        self.coach_name = coach_name

    def set_students_names(students_names):
        self.students_names = students_names

    def set_phone_numbers(phone_numbers):
        self.phone_numbers = phone_numbers

    def get_team_id():
        return self.team_id

    def get_team_name():
        return self.team_name

    def get_coach_name():
        return self.coach_name

    def get_students_names():
        return self.students_names

    def get_phone_numbers():
        return self.phone_numbers

    def send_message(message):
        message.replace("{{team_name}}", self.team_name)
        send_message