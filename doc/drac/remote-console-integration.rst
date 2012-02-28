===============================
 Remote console doesn't launch
===============================


On `plana`
==========

If you don't have a Java plugin in your browser, launching the remote
console just downloads a ``viewer.jnlp(...)`` JNLP_ file.

.. _JNLP: http://en.wikipedia.org/wiki/Java_Web_Start#Java_Network_Launching_Protocol_.28JNLP.29

To run the Java applet, you need::

	sudo apt-get install openjdk-6-jre

To launch the console, run::

	javaws viewer.jnlp*

Note that this is time-sensitive; the authentication token embedded in
the JNLP file will expire in a few seconds.

See also: :doc:`remote-console-keys`.


On `vercoi`
===========

The older DRAC version names the JNLP view ``jviewer.jnlp``. Note that
your browser may rename the file to avoid collisions, e.g. to
``jviewer (1).jnlp``.
