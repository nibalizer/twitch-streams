from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.programming.language import Bash

with Diagram("Falco For Security", show=False):
    source = EKS("Syscall Events")

    with Cluster("Falco"):
        with Cluster("Falco Processing"):
            workers = [ECS("Falco Daemon")]


        queue = SQS("Falco Sidekick")

        with Cluster("Sidekick outputs"):
            handlers = [Lambda("slack"),
                        Lambda("logdna"),
                        Lambda("loki")]

    store = S3("store")
    dw = Redshift("analytics")

    rules = Bash("Rules Definitions")
    source >> workers >> queue >> handlers
    rules >> workers
    handlers >> store
    handlers >> dw

