__version__ = "0.1.10"


import argparse, json, os.path, sys
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
        "-a", "--additional",
        default=None,
        help="path to or URL of an complementary Swagger JSON file",
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

    parser.add_argument(
        "-v", "--version",
        action="version",
        version="swagger2markdown " + __version__
    )

    args = parser.parse_args()

    print("Parsing Swagger JSON... ", end="")

    try:
        swagger_data = json.load(open(args.input, encoding="utf8"))

    except (FileNotFoundError, OSError):
        try:
            swagger_data = requests.get(args.input).json()
        except requests.exceptions.MissingSchema:
            sys.exit('Please specify the URL with schema, e.g. "http://"')
        except requests.exceptions.ConnectionError:
            sys.exit("No Swagger file found.")

    if args.additional:
        try:
            additional_data = json.load(open(args.additional, encoding="utf8"))
        except (FileNotFoundError, OSError):
            try:
                additional_data = requests.get(args.additional).json()
            except requests.exceptions.MissingSchema:
                sys.exit('Please specify the URL with schema, e.g. "http://"')
            except requests.exceptions.ConnectionError:
                sys.exit("No Swagger file found.")
    else:
        additional_data = {}

    swagger_data = {**additional_data, **swagger_data}

    print("Done!")

    print("Parsing the template... ", end="")

    env = jinja2.Environment(extensions=["jinja2.ext.do"])
    template = env.from_string(open(args.template, encoding="utf8").read())

    print("Done!")

    print("Baking Markdown... ", end="")

    with open(args.output, "w", encoding="utf8") as output:
        output.write(template.render(swagger_data=swagger_data))
    print("Done!")

    print("---")

    print("Result: ", args.output)
