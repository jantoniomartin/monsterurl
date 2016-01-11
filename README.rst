monsterurl
==========

**monsterurl** is a tiny, simple application to generate random word groups
to be used in URLs.

The idea comes from Gfycat, a gif hosting service that uses funny names for
its urls:

http://gfycat.com/about#links

Gfycat makes the urls concatenating two adjectives and the name of an animal.

I thought that using monsters instead of animals could be even funnier.

Usage
-----

To use it, simply do::

    >>> from monsterurl import get_monster
    
    >>> print(get_monster())
