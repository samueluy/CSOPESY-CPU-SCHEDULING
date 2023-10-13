class Process:
    def __init__(self, id=None, arrival_time=None, end_time=None, burst_time=None, waiting_time=None, turn_around_time=None):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = waiting_time
        self.end_time = end_time
        self.turn_around_time = turn_around_time

    def get_id(self):
        return self.id

    def set_name(self, id):
        self.id = id

    def get_arrival_time(self):
        return self.arrival_time

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_burst_time(self):
        return self.burst_time

    def set_burst_time(self, burst_time):
        self.burst_time = burst_time