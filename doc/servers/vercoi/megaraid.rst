=====================
 MegaRAID for Vercoi
=====================

To simplify disk space management, the disks in each `vercoi` are
combined in a RAID-5, yielding approximately 1.5 TB of usable space.

As MegaRAID cannot change RAID units currently being used, the easiest
way to configure this is to

- attach a serial console via ``ipmitool``
- reset the server
- during boot press ``control-Y`` for the MegaRAID Preboot CLI
- enter MegaCLI commands to configure the RAID (see later)
- enter ``q`` to quit
- use ``ipmitool`` to power the server off and back on

Note: this erases the disk contents; you will need to reinstall at
this point.

The Preboot CLI takes the same arguments as the ``megacli`` command
line tool, but you leave out the command itself. That is, instead of
``megacli -LdPdInfo -a0`` you type ``-LdPdInfo -a0``.

The MegaCLI commands to configure vercoi are::

  -CfgClr -a0
  -CfgLDDel -Lall -a0
  -CfgLdAdd -r5'[252:0,252:1,252:2,252:3]' WB RA Cached NoCachedBadBBU -a0
