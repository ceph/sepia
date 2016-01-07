New user basics
===============

Set up teuthology
-----------------

#. Request access via the process described at:
   https://github.com/ceph/sepia/blob/master/doc/adding_users.rst

#. Log in to teuthology.front.sepia.ceph.com using the account that was created
   for you (NOT 'ubuntu')

#. Clone teuthology::

     mkdir src
     cd src
     git clone git@github.com:ceph/teuthology
     cd teuthology
     ./bootstrap

#. [Optional] Add $HOME/src/teuthology/virtualenv/bin to your path.

#. Verify it it working::

     teuthology-lock --summary

#. Clone ceph-qa-suite::

     cd ~/src
     git clone git@github.com:ceph/ceph-qa-suite


Lock an individual machine
--------------------------

Lock a machine.  Optionally specify the OS type/version.::

     teuthology-lock --lock-many 1 --machine-type mira | tee mine.yaml

Safely clean up and unlock a machine
------------------------------------

#. Get the bit of yaml for your machine, if you don't already have it handy::

     teuthology-lock --list-targets | tee mine.yaml

#. Nuke, remove, and unlock::

     teuthology-nuke -t mine.yaml -r -u

Run a job on a single machine
-----------------------------

#. Write a job file to a foo.yaml.

#. Get a machine for it::

     teuthology-lock --lock-many NUM --machine-type mira >> foo.yaml

#. Run the test::

     teuthology -v foo.yaml -a foo.yaml.out

#. If it fails, clean up the machine and/or run output::

     teuthology-nuke -t foo.yaml
     rm -r foo.yaml.out


View the queue
--------------

#. From the CLI::

      teuthology-queue -m multi

#. From the web::

      http://pulpito.ceph.com/


Submit a job to the queue
-------------------------

::

     teuthology-schedule myjob.yaml -n myjob -m multi -N NUM

Schedule a test suite
---------------------

#. Schedule.  Note that the kernel branch is optional (you can use
   whatever kernel happens to be installed on the machine). ::

     teuthology-suite -s SUITE -c CEPHBRANCH [-k KERNELBRANCH]

   Part of the output will be the run name, something like::

     zack-2014-07-30_13:33:27-rados-firefly-testing-basic-multi

   Or, to find results from a previous run,::

    ls /a/ | grep $USER

#. View results::

    cd /a/RUNNAME
    ls





  
