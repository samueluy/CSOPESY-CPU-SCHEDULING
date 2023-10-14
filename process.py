class Process:
    def __init__(self, id=None, arrival_time=None, burst_time=None, waiting_time=0, turn_around_time=0):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = waiting_time
        self.turn_around_time = turn_around_time
        self.start_times = []
        self.end_times = []

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_arrival_time(self):
        return self.arrival_time

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_burst_time(self):
        return self.burst_time

    def set_burst_time(self, burst_time):
        self.burst_time = burst_time

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_end_time(self):
        return self.end_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_waiting_time(self):
        return self.waiting_time

    def set_waiting_time(self, waiting_time):
        self.waiting_time = waiting_time

    def get_turn_around_time(self):
        return self.turn_around_time

    def set_turn_around_time(self, turn_around_time):
        self.turn_around_time = turn_around_time

    def add_start_time(self, start_time):
        self.start_times.append(start_time)

    def add_end_time(self, end_time):
        self.end_times.append(end_time)