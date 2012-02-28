=======================
 Using serial consoles
=======================

On `plana`
==========

To start a session::

	ssh root@planaNN.ipmi.sepia.ceph.com -t console com2

Special keys cheat sheet::

	KEY MAPPING FOR CONSOLE REDIRECTION:

	Use the <ESC><0> key sequence for <F10>
	Use the <ESC><!> key sequence for <F11>
	Use the <ESC><@> key sequence for <F12>

	Use the <ESC><Ctrl><M> key sequence for <Ctrl><M>
	Use the <ESC><Ctrl><H> key sequence for <Ctrl><H>
	Use the <ESC><Ctrl><I> key sequence for <Ctrl><I>
	Use the <ESC><Ctrl><J> key sequence for <Ctrl><J>

	Use the <ESC><X><X> key sequence for <Alt><x>, where x is any letter
	key, and X is the upper case of that key

	Use the <ESC><R><ESC><r><ESC><R> key sequence for <Ctrl><Alt><Del>


.. todo:: Move plana to use ipmi sol too, to avoid lockouts?
