#!/usr/bin/env python3
import argparse
import os

import htmlmin
import lesscpy
from jinja2 import Environment, PackageLoader, select_autoescape
from jsmin import jsmin


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="App Builder",
    )
    parser.add_argument(
        "-m",
        "--minify",
        action="store_true",
        help="shrink the app's source code removing unnecesary spaces, etc.",
    )

    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    env = Environment(
        loader=PackageLoader("build", "."),
        autoescape=select_autoescape(["html", "xml"]),
    )
    scripts = []
    for filename in sorted(os.listdir("js")):
        with open(os.path.join("js", filename)) as file:
            if args.minify:
                scripts.append(jsmin(file.read()).replace("\n", ";"))
            else:
                scripts.append(file.read())
    script = ";".join(scripts)

    with open(os.path.join("style", "main.css")) as file:
        if args.minify:
            css = lesscpy.compile(file, minify=True, xminify=True)
        else:
            css = file.read()

    template = env.get_template("index.html.j2")
    html = template.render(css=css, script=script)
    if args.minify:
        html = htmlmin.minify(html)

    if not os.path.exists("dist"):
        os.makedirs("dist")
    with open(os.path.join("dist", "2048.html.w30"), "w") as file:
        file.write(html)
