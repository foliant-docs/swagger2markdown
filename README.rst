################
swagger2markdown
################

Swagger_ is an open specification for documenting REST APIs in JSON or YAML.
Imperfect as it is, it's de facto a standard for many API developers.

This extension lets you render your swagger.json file as a Markdown document.
You can customize the output by providing your own Jinja2_ template.

.. _Swagger: http://swagger.io/
.. _Jinja2: http://jinja.pocoo.org/


.. warning::

    This extension was created for a particular project and thus is only
    guaranteed to work with this particular project! It is very much likely
    you'll have to modify swagger.md.j2_ for your project.

.. _swagger.md.j2: https://github.com/moigagoo/swagger2markdown/blob/master/swagger.md.j2


************
Installation
************

.. code-block:: shell

    $ pip install swagger2markdown


*****
Usage
*****

.. code-block:: shell

    usage: swagger2markdown-script.py [-h] [-i SWAGGER_LOCATION] [-o OUTPUT]
                                    [-t TEMPLATE]

    optional arguments:
      -h, --help            show this help message and exit
      -i SWAGGER_LOCATION, --input SWAGGER_LOCATION
                            path to or URL of the Swagger JSON file (default:
                            swagger.json)
      -o OUTPUT, --output OUTPUT
                            path to the output Markdown file (default: swagger.md)
      -t TEMPLATE, --template TEMPLATE
                            Jinja2 template used for conversion
