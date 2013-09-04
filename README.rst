Meuh!
=====

Meuh is a tool to perform data quality assessments on `Darwin Core Archive`_ (DwC-A) files.

It has the following design goals:

- To be extensible and allow development of new assessment mechanisms by writing a simple Python class.
- To be UI-independent easiy to integrate in a wide range of data flows: command-line tool, web site/services, GUI, batch processing, ...
- Multiple report formats (currently JSON for machines and HTML for human beings). Writing a simple Python class allows to add new report formats.
- To support large data volumes.

Status
------

In heavy development, nothing usable yet.


.. _Darwin Core Archive: http://en.wikipedia.org/wiki/Darwin_Core_Archive