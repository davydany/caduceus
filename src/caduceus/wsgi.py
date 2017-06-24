import logging
import threading
import uuid

from wsgiref import simple_server

from caduceus import BaseClass
from caduceus.monitor.timer import TimerMonitor
from caduceus.monitor.memory import MemoryMonitor

AVAILABLE_MONITORS = (
    TimerMonitor,
    MemoryMonitor
)

logger = logging.getLogger('caduceus')


class RequestThread(threading.Thread):

    def run(self):

        target = self._target
        args = self._args
        self.response = target(*args)

class Caduceus(BaseClass):


    def __init__(self, application, tenant_code):

        self.application = application
        self.tenant_code = tenant_code

    def __call__(self, environ, start_response):

        response_id = str(uuid.uuid4())
        monitors = [MonitorClass() for MonitorClass in AVAILABLE_MONITORS]

        for monitor in monitors:
            monitor.enable_monitor()

        request = RequestThread(target=self.application, args=(environ, start_response, ))
        request.start()
        request.join()
        response = request.response

        for monitor in monitors:
            monitor.disable_monitor()
            monitor.record_metric(response_id)

        print("response: ", response.content)
        return response
