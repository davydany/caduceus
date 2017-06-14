# My Notes

* `WSGIApplicationWrapper` (`from newrelic.api.web_transaction import WSGIApplicationWrapper`) is the wrapper for WSGI apps.

    * The `_nr_wsgi_application_wrapper_` does the initialization:

        * This calls `current_transaction`. 

            * `current_transaction` initializes a `TransactionCache`. 

            * TransactionCache is a great place for getting more information about threads
            like: 
                * getting current thread id
                * active_thread

            * Todo: do some reading about python's weakref module: 
            https://docs.python.org/3/library/weakref.html

        * 