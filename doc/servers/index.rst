=========
 Servers
=========

.. raw:: html

   <style>
     .hardware-diagram td {
       border: solid 1px black !important;
     }

     .hardware-diagram {
       margin-bottom: 2em;
     }
   </style>


.. figure:: overview.jpg
   :width: 40%

   Front view of the row hosting `Sepia`.



Plana
=====

.. figure:: plana-front.jpg
   :width: 70%

   Front of a plana server.

   .. table::
      :class: hardware-diagram

      +--------+------------+-------+--------------+--------------+
      | Serial |            | 2xUSB |              |              |
      +--------+-----+------+-------+--------------+--------------+
      | HDD 0: 500GB | HDD 1: 500GB | HDD 2: 500GB | HDD 3: 500GB |
      +--------------+--------------+--------------+--------------+

.. figure:: plana-back.jpg
   :width: 70%

   Back of a plana server.

   .. table::
      :class: hardware-diagram

      +--------------+----------+-------+----------+--------------------------------------------+
      |              | DRAC     |       | NIC 1g1  | PCI: NIC, A 10g1 (back), B 10g2 (unused)   |
      |              | SD-card  |       | (front)  |                                            |
      +--------+-----+----------+-------+----------+--------------------------------------------+
      |        |     | DRAC     |       | NIC 1g2  |                                            |
      | Serial | VGA | ethernet | 2xUSB | (unused) |                                            |
      +--------+-----+----------+-------+----------+--------------------------------------------+


Burnupi
=======

.. figure:: burnupi-front.jpg
   :width: 70%

   Front of a burnupi server.

   .. table::
      :class: hardware-diagram

      +---------+---------+-----------+------------+--------+
      | HDD 1TB | HDD 1TB | HDD 1TB   | HDD unused | Serial |
      +---------+---------+-----------+------------+--------+
      | HDD 1TB | HDD 1TB | HDD 1TB   | HDD unused | 1xUSB  |
      +---------+---------+-----------+------------+--------+
      | HDD 1TB | HDD 1TB | HD unused | HDD unused |        |
      +---------+---------+-----------+------------+--------+


.. figure:: burnupi-back.jpg
   :width: 70%

   Back of a burnupi server.

   .. table::
      :class: hardware-diagram

      +--------------------------------------------+--------------------------------------------+
      |                                            | PCI 1: unused                              |
      |                                            |                                            |
      +--------------+----------+-------+----------+--------------------------------------------+
      |              | DRAC     |       | NIC 1g1  | PCI 2: NIC, A 10g1 (back), B 10g2 (unused) |
      |              | SD-card  |       | (front)  |                                            |
      +--------+-----+----------+-------+----------+--------------------------------------------+
      |        |     | DRAC     |       | NIC 1g2  | PCI 3: unused                              |
      | Serial | VGA | ethernet | 2xUSB | (unused) |                                            |
      +--------+-----+----------+-------+----------+--------------------------------------------+


Vercoi
=======

.. figure:: vercoi-front.jpg
   :width: 70%

   Front of a vercoi server.

   .. note:: Mapping of hard drives to vercoiNN was done via
      documentation, not verified.

   .. table:: Layout of the disks for blades
      :class: hardware-diagram

      +---------+-------------+-------------+-------------+-------------+
      | chassis | 1: vercoi02 | 2: vercoi04 | 3: vercoi01 | 4: vercoi03 |
      +---------+-------------+-------------+-------------+-------------+
      | chassis | 1: vercoi06 | 2: vercoi08 | 3: vercoi05 | 4: vercoi07 |
      +---------+-------------+-------------+-------------+-------------+

   .. table:: Drives for each blade (2.5", vertical mount)
      :class: hardware-diagram

      +--------------+--------------+--------------+---------------+---------------+---------------+
      | HDD 0: 500GB | HDD 1: 500GB | HDD 2: 500GB |  HDD 3: 500GB | HDD 4: unused | HDD 5: unused |
      +--------------+--------------+--------------+---------------+---------------+---------------+


.. figure:: vercoi-back.jpg
   :width: 70%

   Back of a vercoi server.

   .. table:: Layout of the blades
      :class: hardware-diagram

      +---------+-------------+-------------+
      | chassis | 3: vercoi01 | 1: vercoi02 |
      |         +-------------+-------------+
      |         | 4: vercoi03 | 2: vercoi04 |
      +---------+-------------+-------------+
      | chassis | 3: vercoi05 | 1: vercoi06 |
      |         +-------------+-------------+
      |         | 4: vercoi07 | 2: vercoi08 |
      +---------+-------------+-------------+

   .. table::
      :class: hardware-diagram

      +--------------------------------------+--------------+
      | PCI: NIC, 10g1 (back), 10g2 (unused) | PCI? unused  |
      +-------+--------+--------+------------+--------+-----+
      |       | NIC 1g | NIC 1g | DRAC       |        |     |
      | 2xUSB | (?)    | (?)    | ethernet   | Serial | VGA |
      +-------+--------+--------+------------+--------+-----+


Networking inside the Linux host:

.. graphviz:: vercoi-interfaces.dot
