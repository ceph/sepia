=======
 Plana
=======

.. raw:: html

   <style>
     .hardware-diagram td {
       border: solid 1px black !important;
     }

     .hardware-diagram {
       margin-bottom: 2em;
     }
   </style>


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
