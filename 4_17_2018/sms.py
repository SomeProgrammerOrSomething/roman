class SMS_Store:
	def __init__(self,message_body=[]):
		self.messages = message_body

	def add_msg(self,	from_num,	text_of_message,	arrival_time,	has_been_viewed=[False]):
		self.messages.append( (from_num,	text_of_message,	arrival_time,	has_been_viewed) )

	def msg_count(self):
		return len(self.messages)

	def get_unread_indexes(self):
		for index in range(len(self.messages)):
			if self.messages[index][3][0] == False:
				print index
		return

	def get_msg(self,i):
		if self.messages[i][3][0] == False:
			self.messages[i][3][0] = True
		return self.messages[i]


	def delete(self,i):
		"""Delete the message at index i"""
		del self.messages[i]


	def clear(self):
		"""Delete all messages from inbox."""
		self.messages = []