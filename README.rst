Meuh!
=====

Meuh is a tool to perform data quality assessments on `Darwin Core Archive`_ (DwC-A) files.

It has the following design goals:

- To be extensible and allow development of new assessment mechanisms by writing a simple Python class.
- To be UI-independent easiy to integrate in a wide range of data flows: command-line tool, web site/services, GUI, batch processing, ...
- Easily extensible output formats (currently JSON for machines and HTML for human beings)
- To support large data volumes.

Status
------

In heavy development, nothing usable yet.

Command-line usage
------------------

::

    $ meuh [--report-format {json,html}] config_file data_file

Note: realtime progress and debug info is logged on stderr, while the report is printed on stdout. That allows to follow execution progress in the terminal and store Meuh report in a different file with something like:

::

    $ meuh --report-format json config_py dwca.zip > results.json

As the default output format is JSON, that can be simplified to

::

     $ meuh config_py dwca.zip > results.json



.. _Darwin Core Archive: http://en.wikipedia.org/wiki/Darwin_Core_Archive