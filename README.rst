Django Metrics Dashboard URL-Unshorten Users
============================================

A widget for the django-metrics-dashboard that displays the user count of
urlunshorten.com

Installation
------------

To get the latest stable release from PyPi::

    $ pip install md-urlunshorten-users

To get the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/md-urlunshorten-users.git#egg=md_urlunshorten_users

Add the app to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'md_urlunshorten_users',
    ]

Run the south migrations to create the app's database tables::

    $ ./manage.py migrate md_urlunshorten_users


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 md-urlunshorten-users
    $ pip install -r requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch


Discuss
-------

If you have questions or issues, please open an issue on GitHub.

If we don't react quickly, please don't hesitate to ping me on Twitter
(`@mbrochh <https://twitter.com/mbrochh>`_)
