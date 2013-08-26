=========
 Mira
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


.. figure:: mira-front.jpg
   :width: 70%

   Front of a mira server.

   .. table::
      :class: hardware-diagram

      +---------+---------+---------+---------+
      | HDD 1TB | HDD 1TB | HDD 1TB | HDD 1TB |
      +---------+---------+---------+---------+
      | HDD 1TB | HDD 1TB | HDD 1TB | HDD 1TB |
      +---------+---------+----------+--------+

.. figure:: mira-back.jpg
   :width: 70%

   Back of a mira server.

   .. table::
      :class: hardware-diagram

      +-----------------------------------------------+-----------------------------------------+
      |                                               | PCI-E slots 1-7 (half height)           |
      |                                               |                                         |
      +--------+------+-------------------------------+                                         |
      |        |      |                               |                                         |
      | ps/2   | IPMI |                               |                                         |
      +--------+------+----------+---------+----------+                                         |
      |        |      |          | NIC 1g1 | NIC 1g2  |                                         |
      | ps/2   | USB  | Serial   | (front) | (unused) |                                         |
      +--------+------+----------+---------+----------+-----------------------------------------+
