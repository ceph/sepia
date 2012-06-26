=========
 Network
=========

Overview of the network design for the Sepia lab. You are not expected
to understand this ;)

.. graphviz:: network.dot


VLANs
=====

=========== ===== ===============
name        vlan# subnet
=========== ===== ===============
pub         146   64.90.32.32/27
front       214   10.214.128.0/20
back        2214  10.214.144.0/20
ipmi        414   10.214.0.0/20
switch mgmt 514   172.31.13.0/24
rescue      246   10.246.128.0/20
isolated0   1000  --
isolated1   1001  --
isolated2   1002  --
isolated3   1003  --
isolated4   1004  --
isolated5   1005  --
isolated6   1006  --
isolated7   1007  --
isolated8   1008  --
isolated9   1009  --
=========== ===== ===============
