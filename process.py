class Process:
    def __init__(self, name=None, arrival_time=None, burst_time=None):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_arrival_time(self):
        return self.arrival_time

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_burst_time(self):
        return self.burst_time

    def set_burst_time(self, burst_time):
        self.burst_time = burst_time