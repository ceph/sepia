Using IPMI on physical machines
===============================

Please obtain the password out of band from another lab user.

Power cycling
-------------

::

 ipmitool -H HOSTNAME.ipmi.sepia.ceph.com -I lanplus -U inktank -P PASSWORD power cycle

Serial console
--------------

::

 ipmitool -H HOSTNAME.ipmi.sepia.ceph.com -I lanplus -U inktank -P PASSWORD sol activate

To exit out of the serial console, you need to type ``~.``.  Since
``~`` also a magic value for ssh, you usually need to do ``~~.``.
