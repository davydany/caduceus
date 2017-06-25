from caduceus import BaseClass

__all__ = ['Recorder']

class MetricsRecorder(BaseClass):

    def record(self, request_id, key, value):

        log_record = 'Request: %s :: %s ==> %s' % (request_id, key, value)
        self.logger.info(log_record)

Recorder = MetricsRecorder()