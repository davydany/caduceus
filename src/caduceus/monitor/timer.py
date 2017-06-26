import datetime
from caduceus.monitor import BaseMonitor

class TimerMonitor(BaseMonitor):

    monitor_name = 'timer'

    def enable_monitor(self):

        self.start_time = datetime.datetime.now()

    def disable_monitor(self):

        self.stop_time = datetime.datetime.now()

    @property
    def metrics(self):

        diff = (self.stop_time - self.start_time)
        diff_ms = diff.total_seconds() * 1000
        return {
            'start_time': self.start_time.isoformat(),
            'stop_time': self.stop_time.isoformat(),
            'diff_ms': diff_ms
        }
