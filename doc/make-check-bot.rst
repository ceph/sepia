==============
Make check bot
==============

The make check bot runs on every Ceph pull request and reports the
result of ``make check`` as a comment to the corresponding pull
request.

GitLab instance
===============

A `GitLab instance <http://workbench.dachary.org/>`_ mirrors the main
Ceph git repository and has a web hook signaling a `Jenkins instance
<http://jenkins.ceph.dachary.org/>`_ on each pull request update.

To access ``workbench.dachary.org`` which is hosted on the Red Hat
public cloud::

    ssh -A -p 2222 ubuntu@workbench.dachary.org

The corresponding virtual machine is ``loic-workbench``.

To access ``jenkins.ceph.dachary.org`` which is hosted by the Free
Software Foundation France::

    ssh -A ubuntu@jenkins.ceph.dachary.org

Jenkins Slave
=============

The Ceph jenkins job has a single slave, hosted on rex001. To access it::

    ssh -A loic@rex001.front.lab.lax.redhat.com
    docker exec -t -i slave001 bash


