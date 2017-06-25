.. figure:: https://github.com/davydany/caduceus/raw/master/img/caduceus-logo.png
   :alt: caduceus

Caduceus
========

Caduceus allows you to inspect your HTTP requests and finding more
details about what happens behind the scenes on each of your requests.

Install
-------

.. code:: bash

    pip install --upgrade caduceus

Register
--------

Go to ``caduceus.davydany.com`` to register your application with
Caduceus and get your own tenant ID.

Setup
-----

Change your Django Application’s ``wsgi.py`` to be:

::

    """
    WSGI config for YOUR_PROJECT_NAME project.

    It exposes the WSGI callable as a module-level variable named ``application``.

    For more information on this file, see
    https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
    """

    import os

    from caduceus.wsgi import Caduceus
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YOUR_PROJECT_NAME.settings.dev")

    tenant_id = 'YOUR-TENANT-ID'
    application = Caduceus(get_wsgi_application(), tenant_id)
