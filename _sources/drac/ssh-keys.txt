==================================
 SSH RSA keys must be <=2047 bits
==================================

For iDRAC6 to accept SSH key authorization, the key must be RSA<=2047
bits, or DSA. You may need to create a new SSH key just for that.

To create an RSA key that is 2047 bits long, and store it in ``drac``
and ``drac.pub``::

	ssh-keygen -t rsa -b 2047 -f drac


Apparently DSA, as implemented in OpenSSH, is considered weaker, so
please use RSA. Sources: `1
<http://www.linuxforums.org/forum/security/3515-rsa-versus-dsa.html>`__
`2 <http://meyering.net/nuke-your-DSA-keys/>`__
