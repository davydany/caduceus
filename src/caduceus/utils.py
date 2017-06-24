import os
import sys

from django.conf import settings

SITE_PACKAGES_PATH = [path
                      for path in sys.path
                      if path.endswith('site-packages')][0]


def local_django_apps():
    """
    Finds the Django Apps that are local to the project.
    """

    # EXCLUDE_APPS
    # ------------
    # there are certain apps that don't have their top-level application
    # name the same as the project name. This takes care of those apps.
    EXCLUDE_APPS = ['rest_framework']

    # LOCAL_APPS
    # ----------
    # where we will collect the final set of local apps
    LOCAL_APPS = []

    # now traverse the django BASE_DIR (which is available for all projects)
    for traversal in os.walk(settings.BASE_DIR):

        # traversal = dirpath, dirnames, filenames
        dirpath, dirnames = traversal[0], traversal[1]

        # just get dirs that are also in the INSTALLED_APPS setting that
        # Django uses.
        for dirname in dirnames:

            # again, we don't want to include apps that are in the EXCLUDE_APPS
            if dirname in EXCLUDE_APPS:
                continue

            if dirname in settings.INSTALLED_APPS:

                # we don't want to include packages that are part of site-packages
                abspath_to_dir = os.path.join(dirpath, dirname)
                if SITE_PACKAGES_PATH in abspath_to_dir:
                    continue

                if dirname not in LOCAL_APPS: # avoid duplicates
                    LOCAL_APPS.append(dirname)

    return tuple(LOCAL_APPS)
