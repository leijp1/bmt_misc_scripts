class Student:
	def __init__(self, student_id, name, team):
		self.id = student_id
		self.name = name
		self.team = team

	def set_student_id(self, student_id):
		self.id = student_id

	def set_student_name(self, name):
		self.name = name

	def set_team(self, team):
		self.team = team

	def get_student_id(self):
		return self.id

	def get_student_name(self):
		return self.name

	def get_team(self):
		return self.team