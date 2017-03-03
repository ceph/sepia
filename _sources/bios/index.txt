===============
 BIOS settings
===============

The factory defaults never have serial console enabled. To set up
serial console, you need to use the Java-based remote console. After
that, you can use the serial console.

On plana
========

Go into BIOS by hitting F2 at boot time and change settings to match::

	BIOS / Serial Communication:
	Serial Communication .......... On with Console Redirection via COM2
	Serial Port Address ........... Serial Device1=COM1,Serial Device2=COM2
	External Serial Connector ..... Serial Device2
	Failsafe Baud Rate ............ 115200
	Remote Terminal Type .......... VT100/VT220
	Redirection After Boot ........ Enabled

	BIOS / Boot Settings:
	Boot Mode ..................... BIOS
	Boot Sequence ................. <ENTER>
	Boot Sequence Retry ........... Disabled

	BIOS / Boot Settings / Boot Sequence:

	1. Hard Drive C: (Integrated SAS #02000 ID00 LUN0 ATA)
	2. Embedded NIC 1 MBA v6.0.11  Slot 0100
