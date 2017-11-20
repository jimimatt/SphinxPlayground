Creating Documentation with Sphinx Mini-Tutorial
================================================

1) Create an empty folder **'docs/'**, this is the common place for a documentation.
   Change into the docs-directory.

2) Run **'sphinx-quickstart'** from the command-line, answer the following questions. Most of the time the defaults are fine, but i   would recommend to set **'autodoc'** to *yes* (this includes docstrings from modules automatically). You are able to change settings afterwards in the file *conf.py*.

3) Create the documentation with **'make html'** (this will generate a html-site with starting point *'index.html'*) or you create a pdf-documentation with **'make pdf'** (prerequisite: installed & working *LaTeX*).


The **index.rst** is the backbone of creating documentation with Sphinx: It comprises the structure of the documentation. Here you can include external .rst files or pictures or fetch automatically the docstrings from your python modules.

A sample *index.rst* could look like this:
~~~
Contents:
 
.. toctree::
   :maxdepth: 2
 
.. automodule:: SomeModuleName
 
.. autoclass:: SomeClassName
    :members:
 
Indices and tables
==================
 
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
~~~

More information: [http://www.sphinx-doc.org/en/stable/tutorial.html](http://www.sphinx-doc.org/en/stable/tutorial.html)

Please keep in mind to write your python docstrings as [**reStructuredText**](http://www.sphinx-doc.org/en/stable/rest.html).
