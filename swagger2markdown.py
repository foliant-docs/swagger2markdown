"""Convert a Swagger JSON file into Markdown with Jinja2.

Usage:

swagger2markdown <template> <data> <output>
"""

__version__ = "0.1.0"


import argparse, json, os.path
import jinja2, requests


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i", "--input",
        default="swagger.json",
        help="path to or URL of the Swagger JSON file (default: swagger.json)",
        metavar=""
    )

    parser.add_argument(
        "-o", "--output",
        default="swagger.md",
        help="path to the output Markdown file (default: swagger.md)",
        metavar=""
    )

    parser.add_argument(
        "-t", "--template",
        default=os.path.join(os.path.dirname(__file__), "swagger.md.j2"),
        help="Jinja2 template used for conversion",
        metavar=""
    )

    args = parser.parse_args()

    try:
        swagger_data = json.load(open(args.input, encoding="utf8"))

    except FileNotFoundError:
        swagger_data = requests.get(args.input).json()

    template = jinja2.Template(open(args.template, encoding="utf8").read())

    with open(args.output, "w", encoding="utf8") as output:
        output.write(template.render(swagger_data=swagger_data))
