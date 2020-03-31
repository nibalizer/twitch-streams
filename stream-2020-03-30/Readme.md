# 2020-03-30

## Announcements:

* call for code is focusing on covid-19
* three areas of starter kits
* discord bot is chugging along, help wanted
* cloud functions workshop
* tmux color bit

## New Business:
* Infrastructure as Code
* gitops
 * manifests
 * operators
 * helm charts
* ibm cloud schematics?
 * most of our time was spent working with this: 
   * https://github.com/nibalizer/ibmcloud-terraform/blob/master/main.tf
 * https://github.com/svennam92/ibmcloud-terraform

## If there is time:
* loopback + cloud databases
* appid

```

nibz@nuc:~/projects/twitch/stream-2020-03-30$ ibmcloud is in 0717_c9d96ddd-c5a3-494c-a6f9-34010db51fc1
Getting instance 0717_c9d96ddd-c5a3-494c-a6f9-34010db51fc1 under account IBM as user skrum@us.ibm.com...

ID                           0717_c9d96ddd-c5a3-494c-a6f9-34010db51fc1
Name                         testinstance
Status                       running
Profile                      bx2-2x8
Architecture                 amd64
vCPUs                        2
Memory                       8
Network Performance (Gbps)   4
Image                        ID                                          Name
                             r006-14140f94-fcc4-11e9-96e7-a72723715315   ibm-ubuntu-18-04-1-minimal-amd64-1

VPC                          ID                                          Name
                             r006-9e036f6e-f440-4319-921d-227b61a11e19   nibz

Zone                         us-south-1
Resource group               default
Created                      2020-03-30T22:48:45+00:00
Network Interfaces           Interface   Name                                               ID                                          Subnet    Private IP   Floating IP     Security Groups
                             Primary     slapstick-drench-nuclei-busybody-delegate-likely   0717-9d3a4bf4-7257-45c8-b941-3081ca57bbe5   subnet1   10.240.0.4   52.116.132.39   scope-defender-earthworm-devotion-copilot-muck

Boot volume                  ID                                          Name                                            Attachment ID                               Attachment name
                             r006-9caef09a-72d8-11ea-aad4-feff0b330b12   rocky-dynamic-squander-previous-spoils-deport   0717-0fc3d0bb-1c38-4606-98be-6bb48c1e8f78   volume-attachment

```


## References:

* <https://cloud.ibm.com/docs/schematics?topic=schematics-manage-lifecycle>
* <https://blog.stackpath.com/wp-content/uploads/2020/01/infrastructure-as-code.png>
* <https://github.com/ibm-cloud-docs/terraform>
* <https://cloud.ibm.com/docs/terraform?topic=terraform-vpc-gen2-resources>
* <https://releases.hashicorp.com/terraform/0.11.14/>
* <https://github.com/IBM-Cloud/terraform-provider-ibm/releases>
* <https://github.com/Call-for-Code/cfc-covid-19-quiz-app>
* <https://unix.stackexchange.com/questions/360545/tmux-not-colorizing-ps1-prompt/493472>
* <https://callforcode.org/>
* <https://developer.ibm.com/tutorials/crisis-communication-chatbot-watson-assistant-webhook-integration-discovery-covid-data/>
* <https://mrutkows.gitbook.io/cloud-functions/101-workshop-nodejs/ex3-connecting-actions-to-event-sources>
* <https://github.com/nibalizer/ibmcloud_ps1/blob/master/ibmcloud_prompt.bash>
* <https://github.com/nibalizer/dotfiles/blob/master/old/.myshell.sh>
* <https://ohmyz.sh/>
* <https://github.com/hashicorp/hcl>
* <https://www.terraform.io/docs/configuration/variables.html>
* <https://cloud.ibm.com/docs/schematics?topic=schematics-create-tf-config>
* <https://12factor.net/>
* <https://github.com/nibalizer/trendiest/blob/master/last_file_daemon.py#L33>
* <https://github.com/GoogleContainerTools/skaffold>
* <https://skaffold.dev/docs/references/yaml/>
* <https://arstechnica.com/information-technology/2011/09/sparc-t4-looks-to-be-good-enough-to-stave-off-defections-to-x86-linux/>
* <https://en.wikipedia.org/wiki/Solaris_Containers>
* <https://blog.jessfraz.com/post/containers-zones-jails-vms/>
* <https://ibm-cloud.github.io/tf-ibm-docs/v0.24.4/r/is_floating_ip.html>
* <https://okteto.com/blog/remote-kubernetes-development/>
