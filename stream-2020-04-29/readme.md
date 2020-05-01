# 2020-04-29

## Summary

This stream was focused on part two of customzing a vm image for ibmcloud and playing with the ignition tool inside redhat openshift 4 (based on coreos). A couple cool revelations on the stream: ignition has code for ibmcloud already and the qemu image I was working with had a platform=qemu hardcoded. Brief notes on reproducing a rhcos vm on ibmcloud below:

1) DL image

2) gunzip image

3) Edit image:

3a) From raw qcow2, use NBD to enalbe editing: https://gist.github.com/shamil/62935d9b456a6f9877b5

3b)

```
qemu-nbd --connect=/dev/nbd0 ~nibz/rhcos-4.3.8-x86_64-qemu.x86_64.qcow2
fdisk /dev/nbd0 -l
mkdir /media/p{1,2,3}
mount /dev/nbd0p1 /media/p1
mount /dev/nbd0p3 /media/p2
mount /dev/nbd0p3 /media/p3
```

```
vim ./loader/entries/ostree-1-rhcos.conf
./loader.1/entries/ostree-1-rhcos.conf:options $ignition_firstboot rhcos.root=crypt_rootfs console=tty0 console=ttyS0,115200n8 ignition.platform.id=qemu rd.luks.options=discard ostree=/ostree/boot.1/rhcos/039cc1e4bbdb3119ff487119cc505de2c6691b02c9f0d34ee38bb7674907111c/0
```

(loader  is a symlink to loader.1)

```
umount /media/*
qemu-nbd --disconnect /dev/nbd0
rmmod nbd
```

3c)

edit the kernel boot arg,

```
ignition.platform.id=ibmcloud
```

or

```
ip=192.168.7.20::192.168.7.1:255.255.255.0:bootstrap.ocp4.example.com:enp1s0:none
nameserver=192.168.7.77
coreos.inst.install_dev=vda
coreos.inst.image_url=http://192.168.7.77:8080/install/bios.raw.gz
coreos.inst.ignition_url=http://192.168.7.77:8080/ignition/bootstrap.ign
```

or

something dhcp and custom?

4) Upload to ibmcloud and create image

```
time ibmcloud cos put-object --bucket cloud-vm-images-2 --key rhcos4_2.qcow2 --body rhcos-ibmcloud-4.3.8-x86_64-qemu.x86_64.qcow2
2.3 minutes
```


5) (done via ui) Convert object storage file to image

6) Boot VM


* (done via ui) put ignition config into user-data block

-

## Announcements:

- call for code
- twitch streams repo: <https://github.com/nibalizer/twitch-streams>>>>
- New shell script for ibmcos

## New Business:

- ignition configs for openshift

- <https://github.com/coreos/coreos-assembler/pull/1265>
- <https://github.com/coreos/ignition/pull/905>
- <https://github.com/coreos/coreos-assembler>
- <https://docs.fedoraproject.org/en-US/fedora-coreos/getting-started/#_launching_with_qemu_or_libvirt>
- <https://github.com/RedHatOfficial/ocp4-helpernode/blob/master/docs/quickstart-static.md#install-vms>
- <https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/4.3.8/rhcos-4.3.8-x86_64-qemu.x86_64.qcow2.gz>

## If there is time:

- centos 8 vm
- focal vm

## Links


* <https://coreos.com/validate/>
* <https://cloud.ibm.com/vpc-ext/compute/vs>
* <https://coreos.com/os/docs/latest/cloud-config.html>
* <https://callforcode.org/challenge/>
* <https://github.com/nibalizer/twitch-streams/tree/master/stream-2020-04-27>
* <https://spencerkrum.com/posts/>
* <https://github.com/nibalizer/very_misc_scripts/blob/master/cos-auth.sh>
* <https://www.ioccc.org/years.html#2019>
* <https://coreos.com/ignition/docs/latest/boot-process.html>
* <https://github.com/coreos/ignition>
* <https://github.com/coreos/ignition/blob/master/doc/getting-started.md>
* <https://github.com/coreos/docs/blob/master/os/installing-to-disk.md>
* <https://github.com/qemu/qemu/blob/d75aa4372f0414c9960534026a562b0302fcff29/docs/specs/fw_cfg.txt>
* <https://github.com/coreos/ignition/blob/master/doc/examples.md>
* <https://github.com/coreos/ignition/blob/master/doc/configuration-v3_0.md>
* <http://www.iana.org/assignments/media-types/application/vnd.coreos.ignition+json>
* <https://github.com/coreos/ignition/blob/master/doc/supported-platforms.md>
* <https://github.com/coreos/afterburn>
* <https://github.com/coreos/ignition/pulls>
* <https://github.com/coreos/ignition/issues/767>
* <https://github.com/coreos/ignition/pull/927>
* <https://github.com/coreos/fedora-coreos-docs/pull/45>
* <https://github.com/coreos/fedora-coreos-docs>
* <https://docs.fedoraproject.org/en-US/fedora-coreos/provisioning-azure/>
* <https://github.com/coreos/ignition/blob/master/doc/examples.md>
* <https://github.com/coreos/ignition/blob/master/internal/providers/ibmcloud/ibmcloud.go>
* <https://coreos.com/tectonic/docs/latest/troubleshooting/master-nodes.html>
* <https://access.redhat.com/solutions/4073041>
* <https://cloudinit.readthedocs.io/en/latest/topics/datasources/nocloud.html>
* <https://wiki.archlinux.org/index.php/systemd-boot>
* <https://www.linuxquestions.org/questions/linux-general-1/sound-card-not-detected-after-kernel-recompile-137357/>
* <https://coreos.com/os/docs/latest/customizing-sshd.html>
* <https://docs.fedoraproject.org/en-US/fedora-coreos/>
* <https://access.redhat.com/documentation/en-us/openshift_container_platform/4.3/html/architecture/architecture-installation#installation-process_architecture-installation>
* <https://access.redhat.com/documentation/en-us/openshift_container_platform/4.3/html/architecture/architecture-installation#installation-process_architecture-installation>
* <https://coreos.com/ignition/docs/latest/boot-process.html>
* <https://stackoverflow.com/questions/1251999/how-can-i-replace-a-newline-n-using-sed>
* <https://www.cyberciti.biz/faq/howto-restart-ssh/>
* <https://coreos.com/ignition/docs/latest/migrating-configs.html>
* <https://github.com/coreos/ignition/pull/905/files>
* <https://github.com/coreos/coreos-assembler/pull/1265/files>
* <https://github.com/coreos/coreos-assembler>
* <https://docs.fedoraproject.org/en-US/fedora-coreos/getting-started/#_launching_with_qemu_or_libvirt>
* <https://github.com/RedHatOfficial/ocp4-helpernode/blob/master/docs/quickstart-static.md#install-vms>
* <https://en.wikibooks.org/wiki/QEMU/Images#Mounting_an_image_on_the_host>
* <https://gist.github.com/shamil/62935d9b456a6f9877b5>
* <https://twitter.com/GraysonPeddie/status/1079875947111821313>
