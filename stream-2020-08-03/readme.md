# 2020-08-03

## Summary

- Built and played with `crun`, a c rewrite and replacement for `runc` that uses cgroupsv2

## Announcements:

- Homomorphic Encryption - https://arstechnica.com/gadgets/2020/07/ibm-completes-successful-field-trials-on-fully-homomorphic-encryption/
- crun https://www.redhat.com/sysadmin/introduction-crun

## New Business:

- crun
- buildkit

## If there is time:

- yeeting

## Commands

```bash
./configure --prefix=/home/nibz/projects/twitch/stream-2020-08-03
wget 'https://github.com/opencontainers/umoci/releases/download/v0.4.6/umoci.amd64'
./local/bin/umoci  unpack --image busybox:latest bundle
./local/bin/umoci  unpack --rootless --image busybox:latest bundle
cp default-policy.json  ../default-skopeo-policy.json
skopeo copy docker://busybox:latest oci:busybox:latest
./local/bin/skopeo copy docker://busybox:latest oci:busybox:latest
./local/bin/skopeo help
./local/bin/crun spec
./local/bin/crun run test
./local/bin/crun run test --detach
./local/bin/crun run --help
./local/bin/crun run --detach test
```


## Links

- https://arstechnica.com/gadgets/2020/07/ibm-completes-successful-field-trials-on-fully-homomorphic-encryption/
- https://blog.selectel.com/managing-containers-runc/
- https://developer.ibm.com/blogs/2020-challenge-submissions-are-closed-what-to-watch-for/
- https://en.wikipedia.org/wiki/Btrfs
- https://github.com/containers
- https://github.com/containers/buildah
- https://github.com/containers/crun
- https://github.com/containers/crun/blob/master/crun.1.md
- https://github.com/containers/skopeo
- https://github.com/containers/skopeo/blob/master/install.md
- https://github.com/openSUSE/umoci/releases
- https://github.com/opencontainers/runtime-spec/blob/master/config.md
- https://github.com/opencontainers/umoci/releases
- https://mkdev.me/en/posts/the-tool-that-really-runs-your-containers-deep-dive-into-runc-and-oci-specifications
- https://packages.ubuntu.com/search?suite=bionic&section=all&arch=any&keywords=btrfs&searchon=names
- https://stackoverflow.com/questions/6523939/conditional-variable-define-in-makefile-with-ifeq
- https://wiki.ubuntu.com/Releases
- https://www.google.com/search?ei=hXIoX6ycKZWntQaHz4LYBA&q=runc+config.json+example&oq=runc+config.json+example&gs_lcp=CgZwc3ktYWIQAzICCAA6BggAEBYQHlCdBFiTDWCpDmgAcAB4AIABQogBowSSAQE5mAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwjs8uDr7v_qAhWVU80KHYenAEsQ4dUDCAw&uact=5
- https://www.redhat.com/sysadmin/introduction-crun
- https://www.wolframalpha.com/input/?i=%281+%2B+%28%28x+-+2%29+*+9999%29+%2F+262142%29
