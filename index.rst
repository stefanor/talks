Developer Tools
===============

.fx: title

Developer Tools
---------------

The Unix way
------------

Stefano Rivera

Talk With Beer April 2012

----

A craftsmsan is only as good as his tools
=========================================

.. notes::

    We are all developers.
    Good developers use good tools, and know how to use them well
    If we want to be good developers...

----

Most Software Development isn't writing code
============================================

.. notes::

   A lot of what you learn when you want to be software developer is how to write code.
   But actually...
   Software developers mostly read, understand, and debug code.
   Putting things together.
   Mangling data.

----

Why should I listen to you?
===========================

----

Beer
====

.. notes::

   well, actually. Not everyone is drinking beer.
   And that's a poor excuse, anyway

----

I like nice tools
=================

.. notes::

   I'm a Linux geek.
   I was "that guy" in the CS Masters lab.
   Improving developer infrastructure at yola
   maintain some of Ubuntu's developer tools

----

Unix
====

.. notes::

   Be it Linux or OSX, these days most developers use unix.
   At least, all the cool kids do.
   So, you should know it

----

The command line is scary?
==========================

.. notes::

   Really?
   There's a lot to learn, but you don't have to know everything
   predictable

----

Unix lore
=========

----

Text
====

.. notes::

   Unix works with plan text a lot.
   Text is really easy to type and read.
   When programs use plain text, it's easy to debug

----

Small tools that solve one problem well
=======================================

.. sourcecode:: console

   $ echo hello:there | cut -d: -f 1
   hello

.. notes::

   You probably know this, but it doesn't hurt to go over it.
   Unix tools are very similar to functions in a program.
   A good tool does one thing, predictably.
   It does one thing, but can be composed with other tools

----

Quick to create tools for
=========================

.. notes::

   There's much less UI to design when you are building a command line
   app.
   So it's much easier to make something nice.

----

Learn a text editor
===================

----

vi, emacs, gedit, nedit, who cares
==================================

----

.*([Rr]egular)(?:[Ee]xpressions?)
=================================

.. notes::

   Invaluable on the command line, when programming, and in your editor.
   Some suck, but hey

----

grep
====

.. sourcecode:: console

   $ locate -i talk | wc -l
   3712
   $ locate -i talk | grep -i beer
   /home/stefanor/git/talkwithbeer-2012

.. notes::

   Invaluable on the command line, when programming, and in your editor.

----

ack-grep
========

.. notes::

   ignores vcs
   --python
   preg
   ack-grep --help-types

----

sed
===

.. notes::

   indent a file

----

rename
======

.. sourcecode:: console

   $ ls
   foo_bar.c  foo.c  foo.h
   $ rename 's/foo/baz/' *
   $ ls
   baz_bar.c  baz.c  baz.h

----

vcs
===

----

git
===

----

github
======

----

hg, bzr
=======

----

svn
===

----

Stefano Rivera
==============

You can find me on the Internet.

You can find this talk on github, if you want.

There are no URLs, twitter handles or IRC nicks on this page.
There's a great tool called Google, use it.

.. vi: set et sta sw=3 ts=3:
