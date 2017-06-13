from newrelic.api.transaction import current_transaction
from newrelic.common.object_wrapper import function_wrapper
from newrelic.core.agent import Agent, agent_instance
from newrelic.core.config import global_settings


def wrap_api_call(method, method_name):
    metric_name = 'Supportability/api/%s' % method_name

    @function_wrapper
    def _nr_wrap_api_call_(wrapped, instance, args, kwargs):
        settings = global_settings()

        # agent is not initialized / enabled
        if (settings.debug.disable_api_supportability_metrics or
                not Agent._instance or
                not settings.enabled):
            return wrapped(*args, **kwargs)

        transaction = current_transaction()

        if transaction:
            m = transaction._transaction_metrics.get(metric_name, 0)
            transaction._transaction_metrics[metric_name] = m + 1
        else:
            agent = agent_instance()
            app_name = settings.app_name
            agent.record_custom_metric(app_name, metric_name, {'count': 1})

        return wrapped(*args, **kwargs)

    return _nr_wrap_api_call_(method)
