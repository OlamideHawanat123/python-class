from datetime import *
class MenstrualCycle:
	def __init__(self,start_date,end_date,cycle_length, shortest_cycle_length, period_duration):
		self.start_date = start_date
		self.end_date = end_date
		if 21 <= cycle_length <= 35 and 21 <= shortest_cycle_length <= 35 and 3 >= period_duration <= 5:
			self.cycle_length = cycle_length
			self.shortest_cycle_length = shortest_cycle_length
			self.period_duration = period_duration
		else:
			self.cycle_length = 21
			self.shortest_cycle_length = cycle_length
			self.period_duration = period_duration



	def next_flow_starting_date(self):
		return self.start_date + timedelta(self.cycle_length)

	def next_flow_ending_date(self):
		return self.next_flow_starting_date() + timedelta(self.period_duration)

	def ovulation_date(self):
		return self.next_flow_ending_date() + timedelta(self.cycle_length // 2)




