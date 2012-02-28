=====================================================
 Sepia -- Notes on the test lab for the Ceph project
=====================================================

.. default-domain:: standard

Ceph_ is a unified, distributed storage system that operates on a large
number of hosts connected by a TCP/IP network.

.. _Ceph: http://ceph.com/

`Sepia` is the name we gave to our pool of test machines. It happens
to be both a color and a `genus of cuttlefish`_. When we have
different kinds of hardware in the `sepia` pool, we name them after
individual species in the *sepia* genus, for example `sepia plana`_.

.. _`genus of cuttlefish`: http://en.wikipedia.org/wiki/Sepia_(genus)
.. _`sepia plana`: http://en.wikipedia.org/wiki/Sepia_plana

This repository contains notes on managing and using the "Sepia" lab
of test machines, used by the Ceph project. It is managed as a Sphinx
document tree and stored in a Git repository, to provide a combination
of easy editability, searchability and developer friendliness.

While the Sepia machines are not publicly accessible, we hope to share
tools & knowledge with the greater community. If you are an
independent developer working on Ceph or related projects -- such as
Ceph integration to OpenStack -- do contact us and we might be able to
give you access to the hardware resources of the `sepia` lab. Or an
offer of employment ;)


Contents
========

.. toctree::
   :glob:

   *
