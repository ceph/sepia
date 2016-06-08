Requesting Lab Access
=====================

`File a ticket <http://tracker.ceph.com/projects/lab/issues/new>`_ with these
pieces of information:

#. Whether you are only requesting access to schedule jobs (and view their
   results), or also to run jobs manually. The latter is more restricted in
   that it is usually only granted to core developers.

#. The username you would like to use. This should probably just be the first
   part of your email address, but exceptions are possible.

#. A public SSH key.  You may already have this (cat
   ~/.ssh/id_rsa.pub).  If necessary, you can create a new one on the
   machine you will be connecting from with::

    ssh-keygen -t rsa

#. A hashed VPN password.  See below for how to set this up:

Setting up VPN client
---------------------

#. Install openvpn::

    apt-get install openvpn

   or::

    yum install -y openvpn

#. Get the tarball and extract it::

    cd /etc/openvpn
    wget http://ceph.com/sage/sepia-vpn-client.tar.gz
    tar zxvf sepia-vpn-client.tar.gz

#. Create a new VPN password.  Please use a descriptive user and host below so
   that both you and the lab admins can identify who you are (e.g.,
   sage@flab)::

    sepia/new-client USER@HOST

    and capture its output to include in the ticket.  This is your
    hashed VPN password.

#. Some distros use 'nogroup' in /etc/groups; some use 'nobody'.
   If yours does not use 'nogroup', edit the 'group' line in
   the sepia.conf file created above.

#. Once everything is set at the lab, you can start the VPN with::

    service openvpn start

   or similar (depending on your distro).

Mac/Tunnelblick
---------------

If using Mac/Tunnelblick, this is a way that's been found to work; it
may not be the only way:

#. comment out (add a leading '#' to) the line in /etc/openvpn/sepia.conf that mentions 'secret'::

    # auth-user-pass sepia.client/secret

#. add a new line that contains only::

    auth-user-pass

#. connect with Tunnelblick

#. when prompted for user/pass, enter username MYUSERNAME@MYHOST as above, and for password use the secret contents of the file /etc/openvpn/sepia.client/secret, (do not use the username)

#. click the "Save to keychain" box.

(Alternatively command line openvpn can be used as well with the mac os X tun/tap driver).


Adding users (lab admins)
=========================

#. Add the user's ssh public key to the `keys <https://github.com/ceph/keys>`_ repo

#. Create new user entry under ``lab_users`` (or ``admin_users`` if applicable) in `ceph-sepia-secrets.git/ansible/inventory/group_vars/all.yml <https://github.com/ceph/ceph-sepia-secrets/blob/master/ansible/inventory/group_vars/all.yml>`_::

     # Example:
     - name: uname
       key: https://raw.githubusercontent.com/ceph/keys/master/ssh/uname.pub
       ovpn: uname@host asdf etc.

#. Once both PRs have been merged, make sure your local repos are up to date and run the ansible to add the user to the OpenVPN gateway, teuthology, and testnodes::

     cd <path-to-ceph-cm-ansible>
     ansible-playbook -i <path-to-ceph-sepia-secrets>/ansible/inventory/sepia gateway.yml --tags="users"
     ansible-playbook -i <path-to-ceph-sepia-secrets>/ansible/inventory/sepia teuthology.yml --limit="teuthology*" --tags="user,pubkeys"

#. And if you're feeling generous [*]_::

     ansible-playbook -i <path-to-ceph-sepia-secrets>/ansible/inventory/sepia users.yml

You need not use -i if you have some other way to refer to the sepia
inventory file.

.. [*] Since the ``testnodes`` role, and thus, ``users``, role gets run with each teuthology run, the user account will eventually get added to all the testnodes either way.

See https://github.com/ceph/ceph-cm-ansible/tree/master/roles/users#usage
for further information.
