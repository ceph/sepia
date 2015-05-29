Adding users
============

VPN
---

#. Have user get VPN tarball from

      http://ceph.com/sage/sepia-vpn-client.tar.gz

#. User should extract in /etc/openvpn, follow the directions, and send the key.

#. Add the secret to the VPN config on the gateway.

Create user
-----------

#. Get public ssh key from user, which they can generate from::

    ssh-keygen -t rsa

#. Add to ceph-sepia-secrets.git/ansible/inventory/group_vars/all.yml.  Add to teh `lab_users` section.  Submit a pull request.

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

