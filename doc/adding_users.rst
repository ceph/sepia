Requesting Lab Access
=====================

Send a lab admin an email with two pieces of information:

#. A public SSH key.  You may already have this (cat
   ~/.ssh/id_rsa.pub).  If necessary, you can create a new one on the
   machine you will be connecting from with::

    ssh-keygen -t rsa

#. A VPN secret.  See below for how to set this up:

Setting up VPN client
---------------------

#. Install openvpn::

    apt-get install openvpn

   or::

    yum install -y openvpn

#. Get the tarball and extract it::

    cd /etc/openvpn
    wget http://ceph.com/sage/sepia-vpn-client.tar.gz
    tar zxvf sepia-vpn.client.tar.gz

#. Create a new key.  Please use a descriptive user and host below so
   that both you and the lab admins can identify who you are (e.g.,
   sage@flab)::

    sepia/new-client USER@HOST

#. Send us the private key.

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

#. Install VPN key on the gateway.

#. Add the SSH key to
   ceph-sepia-secrets.git/ansible/inventory/group_vars/all.yml.  Add
   to teh `lab_users` section.  Submit a pull request.

#. Create a user on teuthology.front.sepia.ceph.com::

     adduser --disabled-password USER
     cd /home/USER
     mkdir .ssh
     cat > .ssh/authorized_keys
     <ssh key>
     ^D
     chown -R --reference=. .ssh
     chmod 700 .ssh
     chmod 600 .ssh/*

