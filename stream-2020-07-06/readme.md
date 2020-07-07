# 2020-07-06

## Summary

- Reviewed Call for Code
- Reviewed helm chart PR for falcosecurity
- Built out/understood grpc+python build tooling system
- Updated proto definitions in falco/client-py
- Wrote some code to use new generated python code for grpc

## Announcements:

- Extended Break
- Call for Code final stretch

## New Business:

- Falco Helm Chart
- Falco gRPC unix socket in Helm Chart
- Falco python client w/ grpc

## If there is time:

- https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/20190717-seccomp-ga.md

## Commands

```
python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/helloworld.proto
```

```
$ pip freeze
falco @ file:///home/nibz/projects/twitch/stream-2020-07-06/client-py
grpcio==1.26.0
pkg-resources==0.0.0
protobuf==3.12.2
python-dateutil==2.8.1
six==1.15.0
```

```
python3 setup.py sdist bdist_wheel
pip install -r requirements.txt
pip install .
```


## Links

- unix sockets / fifos
- grpc 
- http://pywren.io/
- https://developer.ibm.com/callforcode/get-started/
- https://developers.google.com/protocol-buffers/docs/pythontutorial#where-to-find-the-example-code
- https://docs.python.org/2/library/string.html
- https://docs.python.org/3/library/exceptions.html
- https://docs.python.org/3/tutorial/errors.html
- https://en.wikipedia.org/wiki/Unix_domain_socket#:~:text=A%20Unix%20domain%20socket%20or,the%20same%20host%20operating%20system.
- https://events.linuxfoundation.org/grpc-conf/
- https://github.com/falcosecurity/charts/issues/27
- https://github.com/falcosecurity/charts/pull/31
- https://github.com/falcosecurity/client-go/pull/43/files
- https://github.com/falcosecurity/client-go/pull/45/files
- https://github.com/falcosecurity/client-go/pull/45/files
- https://github.com/falcosecurity/client-go/pull/45/files
- https://github.com/falcosecurity/client-py
- https://github.com/falcosecurity/client-py/issues/25
- https://github.com/falcosecurity/client-py/issues/35
- https://github.com/falcosecurity/client-py/issues/35
- https://github.com/falcosecurity/client-rs/blob/master/Makefile
- https://github.com/falcosecurity/falco-exporter/pull/33
- https://github.com/falcosecurity/falco/blob/master/userspace/falco/version.proto
- https://github.com/falcosecurity/falco/commit/bdbdf7b8301b37823bc9b7aefe89bab606eaaeb5
- https://github.com/falcosecurity/falco/pull/1217
- https://github.com/falcosecurity/falco/pull/1241
- https://github.com/falcosecurity/falco/pull/872/files#diff-bdedeeb475f89713c729be6dab0962f3
- https://github.com/falcosecurity/falco/tags
- https://github.com/falcosecurity/falcosidekick
- https://github.com/grpc/grpc
- https://github.com/grpc/grpc/issues/15675
- https://github.com/protocolbuffers/protobuf/tree/master/python
- https://grpc.github.io/grpc/python/grpc.html#grpc.UnaryUnaryMultiCallable
- https://grpc.github.io/grpc/python/grpc_asyncio.html
- https://grpc.io/
- https://grpc.io/docs/languages/python/basics/
- https://grpc.io/docs/languages/python/basics/
- https://grpc.io/docs/languages/python/quickstart/
- https://helm.sh/docs/chart_template_guide/control_structures/
- https://packaging.python.org/guides/distributing-packages-using-setuptools/
- https://packaging.python.org/key_projects/#setuptools
- https://packaging.python.org/tutorials/packaging-projects/
- https://pypi.org/project/grpcio/#history
- https://raw.githubusercontent.com/falcosecurity/falco/master/userspace/falco/outputs.proto
- https://raw.githubusercontent.com/falcosecurity/falco/master/userspace/falco/version.proto
- https://serverfault.com/questions/358866/create-unix-named-socket-from-the-command-line
- https://stackoverflow.com/questions/49161633/how-do-i-create-a-protobuf3-timestamp-in-python
- https://stackoverflow.com/questions/49654745/capture-config-error-exception-in-python-behave

