import argparse, json, os.path
import jinja2, requests


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i", "--input",
        default="swagger.json",
        help="path to or URL of the Swagger JSON file (default: swagger.json)",
        metavar="SWAGGER_LOCATION"
    )

    parser.add_argument(
        "-o", "--output",
        default="swagger.md",
        help="path to the output Markdown file (default: swagger.md)",
        metavar="OUTPUT"
    )

    parser.add_argument(
        "-t", "--template",
        default=os.path.join(os.path.dirname(__file__), "swagger.md.j2"),
        help="Jinja2 template used for conversion",
        metavar="TEMPLATE"
    )

    args = parser.parse_args()

    try:
        swagger_data = json.load(open(args.input, encoding="utf8"))

    except (FileNotFoundError, OSError):
        swagger_data = requests.get(args.input).json()

    env = jinja2.Environment(extensions=["jinja2.ext.do"])
    template = env.from_string(open(args.template, encoding="utf8").read())

    with open(args.output, "w", encoding="utf8") as output:
        output.write(template.render(swagger_data=swagger_data))
