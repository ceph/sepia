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

#. Run ansible to create the user::

     cd <path-to-ceph-cm-ansible>
     ansible-playbook -i <path...>ceph-sepia-secrets/ansible/inventory/sepia users.yml

You need not use -i if you have some other way to refer to the sepia
inventory file.

See https://github.com/ceph/ceph-cm-ansible/tree/master/roles/users#usage
for further information.
    
