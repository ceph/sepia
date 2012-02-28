==================================================
 Arrow keys etc don't work in DRAC remote console
==================================================

:Affects: `plana`, maybe `burnupi`; not needed for `vercoi`

The Java remote console GUI client is built against ancient X
libraries, and does not understand arrow keys etc.

Discussion and solution:
http://www.anchor.com.au/blog/2011/03/evil-hack-to-make-arrow-and-sysreq-keys-work-with-a-dell-idrac-kvm-and-linux-desktop/

Summary: fetch and compile the code, and run::

	LD_PRELOAD=/path/to/keycode-hack.so javaws viewew.jnlp*
