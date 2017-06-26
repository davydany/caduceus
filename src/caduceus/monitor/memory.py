import os
import pip
import sys
import sys
import threading

from caduceus.monitor import BaseMonitor
from caduceus.utils import local_django_apps

MEMORY_CACHE = {
    'local_vars' : {}
}

LOCAL_APPS = local_django_apps()

def tracer(frame, event, arg):


    if event == 'return':
        module_name = frame.f_globals["__name__"].lower()

        # PRELIMINARY CHECKS ---------------------------------------------------
        # SKIP OMITTABLE CHECKS
        if not any(module_name.startswith(prefix) for prefix in LOCAL_APPS):
            return tracer

        # Now inspect the application
        for name, value in frame.f_locals.items():
            MEMORY_CACHE['local_vars'][name] = value

    return tracer


class MemoryMonitor(BaseMonitor):

    monitor_name = 'tracer'

    def enable_monitor(self):

        # sys.settrace(tracer)
        threading.settrace(tracer)

    def disable_monitor(self):

        # sys.settrace(None)
        threading.settrace(None)

    @property
    def metrics(self):

        # collect metrics and report the things we want to report
        size_in_bytes = 0
        string_count = 0
        for value in MEMORY_CACHE['local_vars'].values():

            size_in_bytes += sys.getsizeof(value)
            if isinstance(value, (str,)):
                string_count += 1

        return {
            'string_count': string_count,
            'size_in_bytes': size_in_bytes
        }
