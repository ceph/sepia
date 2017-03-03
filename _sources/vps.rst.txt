VMs and containers
==================

:note: Lifted verbatim from old intranet -- edit me later

We have two type of virtual machines in the lab. There are lxc-containers (which are more of a jailed/chroot and not really a VM) and libvirt VM's.

One easy way (there are many) you can figure out if its lxc or libvirt/kvm/qemu if it is running is by running this command on the guest:

cat /proc/cpuinfo  | grep -i model\ name | head -1

On lxc the CPU will be an actual model (the HOST) but on qemu/kvm it will list QEMU Virtual CPU version 1.0.

Figuring out which host the guest is on:

If the machine is a teuthology used VPS, IE: hostname like vpmXXX then this can be found via teuthology:

teuthology-lock --list vpmXXX | grep -i vpshost

All vpm machines are libvirt/qemu/kvm.

If it is not a vpm machine then odds are its on one of the internal VM hosts which are a mix of lxc and libvirt on senta01-04 and vercoi01-08. There is a very simple script on the teuthology server for finding which host its on (hopefully something better in the future). From the teuthology machine:

 vmsearch.sh <guestname>

Console for Libvirt:

There are a variety of ways to manage the libvirt guests. The most GUI friendly one is to install virt-manager on your local machine. From there setup a new connection to the host (type should be ssh with ubuntu username). Virt-manager is pretty strait forward. For those who have machines that libvirt won't run on or you don't want to bother with a GUI you can get access to their VGA via a regular VNC client. You can find out what VNC port its running on by ssh'ing to the host machine and running:

guest=guestname; ps aux | grep -i $guest | grep -v grep | awk -F '-vnc 127.0.0.1:' '{print $2}' | awk '{print $1+5900}'

Just change guestname to which guest you are trying to access. This will print out a port number like 5905. You then can use this value with a ssh tunnel:

ssh -L $portnum:localhost:$portnum ubuntu@<guest host>.front.sepia.ceph.com -N

Which will tunnel the data over SSH, You can then point your VNC client to localhost:$portnum to acess the VGA of the guest.

Power for Libvirt:

The guest can be powercycled via running this command on the host (or alternatively on configured machine like teuthology -c <guest host> added to virsh ran on a different machine):

virsh destroy <guestname>

Yes they chose very bad naming here. Even though it says destroy its really doing a hard power off (losing contents of the memory). There is a power option but that just sends ACPI stuff and won't actually power off the guest in most cases.

virsh start <guestname>

The status of the guests can also be found by running:

virsh list --all

Console/power for lxc:

Console can not be very easily accessed on lxc guests with the way they are configured right now. That being the said since they are a chrooted environment they generally don't need to have the console accessed as they are not running their own kernel and thus are generally up if the host is up and its not hard on the guest (possible fs damage) to shut it down if it is unresponsive for some reason. Actually needing to do anything on these guests is pretty rare.

All LXC commands should be ran on the host of said guest. For guest info (running or not) you can get its status via:

sudo lxc-info -n <guestname>

A guest can be stopped via:

sudo lxc-stop -n <guestname>

To start the guest again run:

sudo lxc-start -d -n <guestname>

If you need to troubleshoot something you can run it without -d so you get console output but there is not an easy way (from what I have seen) to detach from this later so if you want to run it long-term it should probably be done in screen or be prepared to shutdown the guest again to run with -d.
