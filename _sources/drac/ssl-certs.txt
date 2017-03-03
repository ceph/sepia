==================================
 Browser Refuses SSL Certificates
==================================

Problem
=======

Out of the box, DRAC comes with a snakeoil SSL certificate. All the
boxes seem to be signed by the same CA, with the same CN and the same
serial number. Reusing a serial number is something that a CA is not
meant to ever do, hence a lot of browsers will complain about
connecting to the iDRAC web interface *on the second server* you use.


Workaround
==========

With Chromium v18 or later, use this to get a browser instance that
has no memory of previous certificates::

  chromium-browser --temp-profile

Even better: with Firefox,

 * use about:config to set browser.cache.disk_cache_ssl false
 * remove/rename/delete "cert8.db" from your browser profile directory

Now, Firefox will complain, but if you save your acceptance of the
security exception, it will remember for the next login.  Firefox
also seems better about actually being able to launch the Java
remote console application.


Fix
===

Replace iDRAC certificates with ones signed by the local organization
(TODO).

Maybe even use DANE__, to avoid the snakeoil cert problem (TODO).

__ http://www.imperialviolet.org/2011/06/16/dnssecchrome.html


Resources
=========

http://comments.gmane.org/gmane.linux.hardware.dell.poweredge/41969
