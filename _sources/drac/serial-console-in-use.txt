========================================
 How to fix serial console in use error
========================================

Sometimes ``console com2`` claims the serial console is in use, when
it is not.

If the web interface list of open sessions shows the session, kill it
from there.

If not, SSH to DRAC and run::

	racadm racreset
