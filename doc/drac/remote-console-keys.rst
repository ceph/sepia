==================================================
 Arrow keys etc don't work in DRAC remote console
==================================================

:Affects: `plana`, maybe `burnupi`; not needed for `vercoi`

The Java remote console GUI client is built against ancient X
libraries, and does not understand arrow keys etc.

Solution: https://github.com/anchor/idrac-kvm-keyboard-fix

Do this::

	install -d -m0755 ~/src
	cd ~/src
	git clone https://github.com/anchor/idrac-kvm-keyboard-fix.git idrac-kvm-keyboard-fix.git
	cd idrac-kvm-keyboard-fix.git
	make
	cd
	LD_PRELOAD=~/src/idrac-kvm-keyboard-fix.git/keycode-hack.so javaws viewew.jnlp*
