from datetime import datetime,timedelta
class MenstrualCycle:
    def __init__(self,start_date,end_date,cycle_length):
        self.start_date = start_date
        self.end_date = end_date
        self.cycle_length = cycle_length

    def get_ovulation_date(self):
        ovulation_date = self.start_date + timedelta(days=self.cycle_length // 2)
        return ovulation_date

    def get_safe_period_start_date(endate):
        return endate + timedelta(days=1)


    def get_safe_period_end_date(self):
        return self.end_date + timedelta(days=6)

    def get_next_period_start_date(self):
        return self.start_date+ timedelta(days=self.cycle_length)


    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_fertile_window(self):
        ovulation_date = self.get_ovulation_date()
        fertile_start = ovulation_date - timedelta(days=5)
        fertile_end = ovulation_date + timedelta(days=1)
        return fertile_start, fertile_end


from datetime import datetime, timedelta


class MenstrualCycle:
    def __init__(self, start_date, end_date, cycle_length):
        self.start_date = start_date
        self.end_date = end_date
        self.cycle_length = cycle_length

    def get_ovulation_date(self):
        ovulation_date = self.end_date + timedelta(days=self.cycle_length // 2)
        return ovulation_date

    def get_safe_period_start_date(endate):
        return endate + timedelta(days=1)

    def get_safe_period_end_date(self):
        return self.end_date + timedelta(days=6)

    def get_next_period_start_date(self):
        return self.start_date + timedelta(days=self.cycle_length)

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_fertile_window(self):
        ovulation_date = self.get_ovulation_date()
        fertile_start = ovulation_date - timedelta(days=5)
        fertile_end = ovulation_date + timedelta(days=1)
        return fertile_start, fertile_end






