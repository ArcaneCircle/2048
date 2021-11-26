#!/usr/bin/env python3
import argparse
import os
from io import StringIO

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
            scripts.append(file.read())
    script = "\n".join(scripts)
    if args.minify:
        script = jsmin(script).replace("\n", ";")

    styles = []
    for filename in sorted(os.listdir("style")):
        with open(os.path.join("style", filename)) as file:
            styles.append(file.read())
    css = "\n".join(styles)
    if args.minify:
        css = lesscpy.compile(StringIO(css), minify=True, xminify=True)

    html = env.get_template("index.html.j2").render(css=css, script=script)
    if args.minify:
        html = htmlmin.minify(html)

    if not os.path.exists("dist"):
        os.makedirs("dist")
    with open(os.path.join("dist", "2048.html.w30"), "w") as file:
        file.write(html)
