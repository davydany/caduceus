from caduceus import BaseClass
from caduceus.recorder import Recorder

class BaseMonitor(BaseClass):
    """
    BaseMonitor.
    """

    # Name of the monitor.
    # Must not have spaces, but instead dashes.
    monitor_name = ''

    def enable_monitor(self):
        '''
        Enables the monitor.
        '''
        raise NotImplementedError()

    @property
    def metrics(self):
        '''
        Returns the metrics collected by the monitor. Data must be returned as 
        a python dictionary
        '''
        raise NotImplementedError()

    def disable_monitor(self):
        '''
        Disables the monitor.
        '''
        raise NotImplementedError()

    def handle_monitor_exception(self, exc_type, exc_val, exc_tb):
        '''
        Handles any exception that the monitor experiences.
        '''
        return

    def record_metric(self, request_id):
        '''
        Performs action to record Metrics collected by this Monitor.
        '''
        Recorder.record(request_id, self.monitor_name, self.metrics)

from caduceus.monitor.timer import TimerMonitor
from caduceus.monitor.memory import MemoryMonitor