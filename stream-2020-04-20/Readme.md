# 2020-04-20


## Announcements:

* call for code, with covid-19 emphasis
* ytt
* k8s lens
* securedns shutting down
* quad9 dns

## New Business:
* falco open source work
* review prs on event-generator
* test out k8s audit system

## Summary

The big goal for this stream was to evaluate some pull requests for the `falcosecurity/event-generator` repository. After that the goal was to set up falco k8s event auditing. This came in two parts, first, configuring the IBM Cloud Kubernetes service to send audit logs at all, then to configure falco to receive them. IBM Cloud Kubernetes Service (IKS) can be configured using one of the cool commands below. Falco can be configured with a one line change in the helm chart.


## Cool Commands:

```bash
ibmcloud ks cluster master audit-webhook set --cluster <cluster_name_or_ID> --remote-server http://172.21.xxx.xxx
```

## Useful links:

* <https://github.com/IBM-Cloud/kube-samples/>
* <https://get-ytt.io/>
* <https://github.com/kubernetes-sigs/kustomize>
* <https://k8slens.dev/>
* <https://quad9dns.quad9.net/dns/>
* <9.9.9.9>
* <https://cloud.ibm.com/docs/containers?topic=containers-health#webhook_logdna>
* <https://k8slens.dev/>
* <https://developer.ibm.com/callforcode/getstarted/covid-19/>
* <https://get-ytt.io/>
* <https://k14s.io/>
* <https://github.com/k14s/ytt>
* <https://github.com/kubernetes-sigs/kustomize>
* <https://securedns.eu/>
* <https://quad9dns.quad9.net/dns/>
* <https://github.com/falcosecurity/event-generator>
* <https://github.com/falcosecurity/event-generator/pull/12/files>
* <https://github.com/falcosecurity/event-generator/blob/master/events/k8saudit/yaml_loader.go>
* <https://github.com/falcosecurity/falco/blob/master/docker/event-generator/k8s_event_generator.sh>
* <https://kubernetes.io/docs/tasks/debug-application-cluster/audit/>
* <https://github.com/falcosecurity/event-generator/pull/14>
* <https://falco.org/docs/event-sources/kubernetes-audit/>
* <https://github.com/falcosecurity/falco/blob/master/examples/k8s_audit_config/README.md#instructions-for-kubernetes-113>
* <https://github.com/falcosecurity/falco/blob/master/examples/k8s_audit_config/audit-policy.yaml>
* <https://falco.org/docs/configuration/>
* <https://cloud.ibm.com/docs/containers?topic=containers-health>
* <https://github.com/IBM-Cloud/kube-samples/blob/master/kube-audit/kube-audit-policy.yaml>
* <https://github.com/kubernetes/kubectl>
* <https://github.com/kubernetes/client-go/blob/master/examples/create-update-delete-deployment/main.go>
* <https://github.com/kubernetes/client-go/blob/master/examples/create-update-delete-deployment/main.go#L37>
