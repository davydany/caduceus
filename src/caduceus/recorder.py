import json
import requests

from caduceus import BaseClass
from caduceus.config import Configuration

__all__ = ['Recorder']

records = {}


class MetricsRecorder(BaseClass):

    def record(self, request_id, key, value):

        # save the record
        if request_id not in records:
            records[request_id] = {}
        records[request_id][key] = value

        # now log to the logger
        log_record = 'Request: %s :: %s ==> %s' % (request_id, key, value)
        print(log_record)
        print("records[%s][%s] = %s" % (request_id, key, value))
        self.logger.info(log_record)

    def flush(self, project_id, request_id, debug=None, report=True):

        config = Configuration(debug)
        print(records)

        # check that we have the request_id in our records
        if request_id not in records:
            self.logger.error(
                "Unable to flush records because '%s' does not exist in the MetricsRecorder Dictionary" % request_id)
            return False

        # log the information
        for key, value in records[request_id].items():
            self.logger.info("Request (%s): %s ==> %s" % (request_id, key, value))

        # collect the details we want to send up
        if report:
            metrics = json.dumps({ request_id : records[request_id] })
            print("Metrics: ", metrics)
            url = config.get_caduceus_remote_url(project_id)
            headers = {'Content-type': 'application/json' }
            response = requests.post(url, data=metrics, headers=headers)
            print("RESPONSE: ", response.content)

        # remove the record
        del records[request_id]


Recorder = MetricsRecorder()
