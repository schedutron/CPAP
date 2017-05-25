.. image:: http://www.attrs.org/en/latest/_static/attrs_logo.png
   :alt: attrs Logo

==================================
attrs: Classes Without Boilerplate
==================================

.. image:: https://readthedocs.org/projects/attrs/badge/?version=stable
   :target: http://www.attrs.org/en/stable/?badge=stable
   :alt: Documentation Status

.. image:: https://travis-ci.org/python-attrs/attrs.svg?branch=master
   :target: https://travis-ci.org/python-attrs/attrs
   :alt: CI Status

.. image:: https://codecov.io/github/python-attrs/attrs/branch/master/graph/badge.svg
   :target: https://codecov.io/github/python-attrs/attrs
   :alt: Test Coverage

.. teaser-begin

``attrs`` is the Python package that will bring back the **joy** of **writing classes** by relieving you from the drudgery of implementing object protocols (aka `dunder <https://nedbatchelder.com/blog/200605/dunder.html>`_ methods).

Its main goal is to help you to write **concise** and **correct** software without slowing down your code.

.. -spiel-end-

For that, it gives you a class decorator and a way to declaratively define the attributes on that class:

.. -code-begin-

.. code-block:: pycon

   >>> import attr
   >>> @attr.s
   ... class Point(object):
   ...     x = attr.ib(default=42)
   ...     y = attr.ib(default=attr.Factory(list))
   ...
   ...     def hard_math(self, z):
   ...         return self.x * self.y * z
   >>> pt = Point(x=1, y=2)
   >>> pt
   Point(x=1, y=2)
   >>> pt.hard_math(3)
   6
   >>> pt == Point(1, 2)
   True
   >>> pt != Point(2, 1)
   True
   >>> attr.asdict(pt)
   {'x': 1, 'y': 2}
   >>> Point()
   Point(x=42, y=[])
   >>> C = attr.make_class("C", ["a", "b"])
   >>> C("foo", "bar")
   C(a='foo', b='bar')


After *declaring* your attributes ``attrs`` gives you:

- a concise and explicit overview of the class's attributes,
- a nice human-readable ``__repr__``,
- a complete set of comparison methods,
- an initializer,
- and much more,

*without* writing dull boilerplate code again and again and *without* runtime performance penalties.

This gives you the power to use actual classes with actual types in your code instead of confusing ``tuple``\ s or confusingly behaving ``namedtuple``\ s.
Which in turn encourages you to write *small classes* that do `one thing well <https://www.destroyallsoftware.com/talks/boundaries>`_.
Never again violate the `single responsibility principle <https://en.wikipedia.org/wiki/Single_responsibility_principle>`_ just because implementing ``__init__`` et al is a painful drag.


.. -testimonials-

Testimonials
============

  I’m looking forward to is being able to program in Python-with-attrs everywhere.
  It exerts a subtle, but positive, design influence in all the codebases I’ve see it used in.

  -- Glyph Lefkowitz, creator of `Twisted <https://twistedmatrix.com/>`_ and Software Developer at Rackspace in `The One Python Library Everyone Needs <https://glyph.twistedmatrix.com/2016/08/attrs.html>`_


  I'm increasingly digging your attr.ocity. Good job!

  -- Łukasz Langa, prolific CPython core developer and Production Engineer at Facebook


  Writing a fully-functional class using ``attrs`` takes me less time than writing this testimonial.

  -- Amber Hawkie Brown, Twisted Release Manager and Computer Owl


.. -end-

.. -project-information-

Project Information
===================

``attrs`` is released under the `MIT <https://choosealicense.com/licenses/mit/>`_ license,
its documentation lives at `Read the Docs <http://www.attrs.org/>`_,
the code on `GitHub <https://github.com/python-attrs/attrs>`_,
and the latest release on `PyPI <https://pypi.org/project/attrs/>`_.
It’s rigorously tested on Python 2.7, 3.4+, and PyPy.

If you'd like to contribute you're most welcome and we've written `a little guide <http://www.attrs.org/en/latest/contributing.html>`_ to get you started!


Release Information
===================

17.1.0 (2017-05-16)
-------------------

To encourage more participation, the project has also been moved into a `dedicated GitHub organization <https://github.com/python-attrs/>`_ and everyone is most welcome to join!

``attrs`` also has a logo now!

.. image:: http://www.attrs.org/en/latest/_static/attrs_logo.png
   :alt: attrs logo


Backward-incompatible changes:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``attrs`` will set the ``__hash__()`` method to ``None`` by default now.
  The way hashes were handled before was in conflict with `Python's specification <https://docs.python.org/3/reference/datamodel.html#object.__hash__>`_.
  This *may* break some software although this breakage is most likely just surfacing of latent bugs.
  You can always make ``attrs`` create the ``__hash__()`` method using ``@attr.s(hash=True)``.
  See `#136`_ for the rationale of this change.

  .. warning::

    Please *do not* upgrade blindly and *do* test your software!
    *Especially* if you use instances as dict keys or put them into sets!

- Correspondingly, ``attr.ib``'s ``hash`` argument is ``None`` by default too and mirrors the ``cmp`` argument as it should.


Deprecations:
^^^^^^^^^^^^^

- ``attr.assoc()`` is now deprecated in favor of ``attr.evolve()`` and will stop working in 2018.


Changes:
^^^^^^^^

- Fix default hashing behavior.
  Now *hash* mirrors the value of *cmp* and classes are unhashable by default.
  `#136`_
  `#142 <https://github.com/python-attrs/attrs/issues/142>`_
- Added ``attr.evolve()`` that, given an instance of an ``attrs`` class and field changes as keyword arguments, will instantiate a copy of the given instance with the changes applied.
  ``evolve()`` replaces ``assoc()``, which is now deprecated.
  ``evolve()`` is significantly faster than ``assoc()``, and requires the class have an initializer that can take the field values as keyword arguments (like ``attrs`` itself can generate).
  `#116 <https://github.com/python-attrs/attrs/issues/116>`_
  `#124 <https://github.com/python-attrs/attrs/pull/124>`_
  `#135 <https://github.com/python-attrs/attrs/pull/135>`_
- ``FrozenInstanceError`` is now raised when trying to delete an attribute from a frozen class.
  `#118 <https://github.com/python-attrs/attrs/pull/118>`_
- Frozen-ness of classes is now inherited.
  `#128 <https://github.com/python-attrs/attrs/pull/128>`_
- ``__attrs_post_init__()`` is now run if validation is disabled.
  `#130 <https://github.com/python-attrs/attrs/pull/130>`_
- Added ``attr.validators.in_(options)`` that, given the allowed `options`, checks whether the attribute value is in it.
  This can be used to check constants, enums, mappings, etc.
  `#181 <https://github.com/python-attrs/attrs/pull/181>`_
- Added ``attr.validators.and_()`` that composes multiple validators into one.
  `#161 <https://github.com/python-attrs/attrs/issues/161>`_
- For convenience, the ``validator`` argument of ``@attr.s`` now can take a ``list`` of validators that are wrapped using ``and_()``.
  `#138 <https://github.com/python-attrs/attrs/issues/138>`_
- Accordingly, ``attr.validators.optional()`` now can take a ``list`` of validators too.
  `#161 <https://github.com/python-attrs/attrs/issues/161>`_
- Validators can now be defined conveniently inline by using the attribute as a decorator.
  Check out the `examples <http://www.attrs.org/en/stable/examples.html#validators>`_ to see it in action!
  `#143 <https://github.com/python-attrs/attrs/issues/143>`_
- ``attr.Factory()`` now has a ``takes_self`` argument that makes the initializer to pass the partially initialized instance into the factory.
  In other words you can define attribute defaults based on other attributes.
  `#165`_
- Default factories can now also be defined inline using decorators.
  They are *always* passed the partially initialized instance.
  `#165`_
- Conversion can now be made optional using ``attr.converters.optional()``.
  `#105 <https://github.com/python-attrs/attrs/issues/105>`_
  `#173 <https://github.com/python-attrs/attrs/pull/173>`_
- ``attr.make_class()`` now accepts the keyword argument ``bases`` which allows for subclassing.
  `#152 <https://github.com/python-attrs/attrs/pull/152>`_
- Metaclasses are now preserved with ``slots=True``.
  `#155 <https://github.com/python-attrs/attrs/pull/155>`_

.. _`#136`: https://github.com/python-attrs/attrs/issues/136
.. _`#165`: https://github.com/python-attrs/attrs/issues/165

`Full changelog <http://www.attrs.org/en/stable/changelog.html>`_.

Credits
=======

``attrs`` is written and maintained by `Hynek Schlawack <https://hynek.me/>`_.

The development is kindly supported by `Variomedia AG <https://www.variomedia.de/>`_.

A full list of contributors can be found in `GitHub's overview <https://github.com/python-attrs/attrs/graphs/contributors>`_.

It’s the spiritual successor of `characteristic <https://characteristic.readthedocs.io/>`_ and aspires to fix some of it clunkiness and unfortunate decisions.
Both were inspired by Twisted’s `FancyEqMixin <https://twistedmatrix.com/documents/current/api/twisted.python.util.FancyEqMixin.html>`_ but both are implemented using class decorators because `sub-classing is bad for you <https://www.youtube.com/watch?v=3MNVP9-hglc>`_, m’kay?


