rewrite
=======

Have you ever wish you could run:

     frob foo.txt > foo.txt

and have it work? But it doesn't, so you have to redirect the output
to some temporary file and then move the result into place? `rewrite`
is a script to do this hard manual labor for you.

Installation
------------

There isn't any. Just copy `src/rewrite.py` into your path somewhere,
and rename it to just `rewrite` if you wish. Or leave it where it is
now and just specify the path.

Usage
-----

Running `rewrite file.txt some-command --bar` will, behind the scenes:

* Execute `some-command --bar file.txt`
* Redirect the standard output of `some-command` to a temporary file
* When `some-command` completes, move the temporary file to `file.txt`

See the included manpage for more information and other ways to run
it.
