import logging
import threading
import uuid

from wsgiref import simple_server

from caduceus import BaseClass
from caduceus.monitor.timer import TimerMonitor
from caduceus.monitor.memory import MemoryMonitor
from caduceus.recorder import Recorder, MetricsRecorder

AVAILABLE_MONITORS = (
    TimerMonitor,
    MemoryMonitor
)

logger = logging.getLogger('caduceus')


class RequestThread(threading.Thread):

    def __init__(self, *args, **kwargs):

        super(RequestThread, self).__init__(*args, **kwargs)

        # default error message (easier for debugging)
        self.response = "Request Failed due to Caduceus"

    def run(self):

        application = self._target
        args = self._args
        self.response = application(*args)

class Caduceus(BaseClass):

    def __init__(self, application, project_id, activate=True, debug=False, report=True):

        self.application = application
        self.project_id = project_id

        self.activate = activate
        self.debug = debug
        self.report = report

    def __call__(self, environ, start_response):

        if self.activate:
            # only run Caduceus if we have it activated.
            response_id = str(uuid.uuid4())
            monitors = [MonitorClass() for MonitorClass in AVAILABLE_MONITORS]

            for monitor in monitors:
                monitor.enable_monitor()

            request = RequestThread(target=self.application, args=(environ, start_response, ))
            request.start()
            request.join()
            response = request.response
            # response = self.application(environ, start_response)

            for monitor in monitors:
                monitor.disable_monitor()
                monitor.record_metric(response_id)

            Recorder.flush(self.project_id, response_id, debug=self.debug, report=self.report)
            return response

        else:
            response = self.application(environ, start_response)
            return response