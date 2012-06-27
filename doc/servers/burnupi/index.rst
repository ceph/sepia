=========
 Burnupi
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
