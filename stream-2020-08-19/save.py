import os
import requests

from fedora_messaging import config

ttvopenfeed_host = "localhost:3000"



class SaveMessage(object):
    """
    A fedora-messaging consumer that saves the message to a file.

    A single configuration key is used from fedora-messaging's
    "consumer_config" key, "path", which is where the consumer will save
    the messages::

        [consumer_config]
        path = "/tmp/fedora-messaging/messages.txt"
    """

    def __init__(self):
        """Perform some one-time initialization for the consumer."""
        self.path = config.conf["consumer_config"]["path"]

        # Ensure the path exists before the consumer starts
        if not os.path.exists(os.path.dirname(self.path)):
            os.mkdir(os.path.dirname(self.path))

    def __call__(self, message):
        """
        Invoked when a message is received by the consumer.

        Args:
            message (fedora_messaging.api.Message): The message from AMQP.
        """
        #requests.post("http://" + ttvopenfeed_host + "/submit", json={"message": ev_str})
        #from pdb import set_trace; set_trace()

        # handle comment added
        if message.topic == 'org.fedoraproject.prod.pagure.pull-request.comment.added':
            print(message.body)
            # body.
            print(message.body["pullrequest"]["comments"]["comment"])

        #print(message.topic)

        #if 'pull-request' in message.topic:
        #    print(message)

        #with open(self.path, "a") as fd:
        #    fd.write(str(message))
