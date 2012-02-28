=====================================
 Remote console loses keyboard focus
=====================================

:Affects: `plana`, `vercoi`; most likely `burnupi` too

The Java remote console client loses keyboard focus if the mouse goes
outside the window. To regain focus, click the menus.

On the `plana` version, you know it worked if you see this debug
message::

	02/08/2012 02:03:16:263:  Sending input focus message with focus set to: true
