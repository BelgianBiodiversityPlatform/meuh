Using meuh on the command-line
------------------------------

::

    $ meuh [--report-format {json,html}] config_file data_file

Note: realtime progress and debug info is logged on stderr, while the report is printed on stdout. That allows to follow execution progress in the terminal and store Meuh report in a different file with something like:

::

    $ meuh --report-format json config_py dwca.zip > results.json

As the default output format is JSON, that can be simplified to

::

     $ meuh config_py dwca.zip > results.json