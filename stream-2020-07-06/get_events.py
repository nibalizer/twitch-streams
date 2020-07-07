import argparse

import falco

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-format", "-o", dest="output_format", default=None, help="output_format")
    args = parser.parse_args()

    c = falco.Client(
        endpoint="unix:///tmp/foo",
        output_format=args.output_format,
    )

    for event in c.subscribe(falco.Request()):
        print(event)
