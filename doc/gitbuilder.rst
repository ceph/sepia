
Notes creating gitbuilder-ceph-rpm-fedora22-amd64-basic
-------------------------------------------------------

These are the steps I took to create a fedora 22 builder.  YMMV for other distros.

Some/most of this should be automated in the fabfile... except that we
likely want to replace that with some other tool that also/instead
does jenkins builders, so I'm not inclined to invest in adding it
right now.

#. meta file::
 cat > meta-data
 downburst:
   disk-size: 40G
   cpus: 4
   ram: 16G
   distro: fedora
   distroversion: "22"
   arch: x86_64
   networks:
     - source: front

#. user file::

  cat > user-data
  user: ubuntu

#. downburst it::

  git clone git://github.com/ceph/downburst
  cd downburst
  ./bootstrap
  sudo virtualenv/bin/downburst -v create --user-data user-data --meta-data meta-data gitbuilder-ceph-rpm-fedora22-amd64-basic

#. connect::

  ubuntu@irvingi07:~/downburst$ ssh ubuntu@gitbuilder-ceph-rpm-fedora22-amd64-basic.front.sepia.ceph.com

#. install ssh keys (be sure to include ubuntu@teuthology)::

  cat >> .ssh/authorized_keys
  ...

#. install redhat-lsb::

  sudo dnf install -y redhat-lsb

#. make sure 'wheel' group doesn't need a password for sudo, like so::

  %wheel  ALL=(ALL)       NOPASSWD: ALL

#. disable selinux (set SELINUX=disabled)::

  sudo vi /etc/selinux/config
  sudo reboot

#. add autobuild-ceph user to group wheel::

  sudo vi /etc/group

#. add gitbuilder to fabfile.py list at the top

#. run fab.  ensure you have gnupg *.gpg and rsync-key[.pub] in your autobuild-ceph checkout::

  bin/fab gitbuilder_ceph_rpm:host=ubuntu@gitbuilder-ceph-rpm-fedora22-amd64-basic.front.sepia.ceph.com

#. set up lighttpd::

  bin/fab gitbuilder_serve_rpm:host=ubuntu@gitbuilder-ceph-rpm-fedora22-amd64-basic.front.sepia.ceph.com

#. set up junit4.jar symlink::

  sudo ln -s junit.jar /usr/share/java/junit4.jar
