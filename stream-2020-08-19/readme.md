# 2020-08-19

## Summary

- Played with the Diagrams tool. It was cool if not perfect.
- Upgraded and improved the open source feed app
- Started to build an open source feed app worker for fedora-messaging
-- Identified fedora-messaging as the successor to fedmesg
-- Pulled certs from the repo
-- Discovered you can do `--callback-file` and not mess with python paths

## Announcements:

- Building Band Aide moving to Mondays

## New Business:

- https://github.com/mingrammer/diagrams
-- we checked it out! It's rad
-- quick reference sheet falco architecture
- Open source feed graph website
- falco python build

## If there is time:

- falco buildkit

## Commands

```bash
fedora-messaging --conf config.toml consume --callback-file=save.py:SaveMessage
```


## Links

- http://192.168.0.12:3000/web
- http://192.168.0.12:3000/socketio
- https://bitbucket.org/chromiumembedded/cef/src/master/
- https://camo.githubusercontent.com/6b7ec40836904a4ebf59bebf0837347f63a3f384/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f70726f76696465722d4f7261636c65436c6f75642d6f72616e67653f6c6f676f3d6f7261636c6526636f6c6f723d663830303030
- https://diagrams.mingrammer.com/docs/getting-started/examples
- https://diagrams.mingrammer.com/docs/getting-started/installation#quick-start
- https://diagrams.mingrammer.com/docs/getting-started/installation#quick-start
- https://diagrams.mingrammer.com/docs/nodes/onprem
- https://diagrams.mingrammer.com/img/advanced_web_service_with_on-premise_colored.png
- https://docs.github.com/en/rest/reference/activity#events
- https://falco.org/
- https://falco.org/images/logos/falco-logo.png
- https://fedora-messaging.readthedocs.io/en/latest/#user-guide
- https://fedora-messaging.readthedocs.io/en/latest/configuration.html#conf-bindings
- https://fedora-messaging.readthedocs.io/en/latest/configuration.html#conf-callback
- https://fedora-messaging.readthedocs.io/en/latest/consuming.html
- https://fedora-messaging.readthedocs.io/en/latest/installation.html#pypi
- https://fedora-messaging.readthedocs.io/en/latest/quick-start.html
- https://fedora-messaging.readthedocs.io/en/stable/consuming.html
- https://github.com/falcosecurity/falcosidekick
- https://github.com/fedora-infra/fedora-messaging
- https://github.com/fedora-infra/fedora-messaging/blob/stable/configs/fedora-cert.pem   
- https://github.com/fedora-infra/fedora-messaging/blob/stable/fedora_messaging/cli.py#L197
- https://github.com/fedora-infra/fedora-messaging/tree/stable/configs
- https://github.com/kubernetes/
- https://github.com/mingrammer/diagrams/tree/master/resources/k8s
- https://github.com/mingrammer/diagrams/tree/master/resources/programming/language
- https://github.com/nibalizer/opensourcefeed/issues
- https://github.com/nibalizer/opensourcefeed/issues/2
- https://github.com/nibalizer/opensourcefeed/issues/4
- https://github.com/nibalizer/opensourcefeed/issues/5
- https://github.com/nibalizer/opensourcefeed/issues/6
- https://github.com/onedesign/express-socketio-tutorial
- https://github.com/socketio/chat-example/blob/master/index.html
- https://graphviz.gitlab.io/download/
- https://landscape.cncf.io/
- https://learn.jquery.com/using-jquery-core/manipulating-elements/
- https://pagure.io/fesco
- https://raw.githubusercontent.com/fedora-infra/fedora-messaging/master/configs/fedora-cert.pem
- https://raw.githubusercontent.com/fedora-infra/fedora-messaging/master/configs/fedora-key.pem
- https://superuser.com/questions/1305902/render-a-web-page-on-top-of-a-video-using-ffmpeg
