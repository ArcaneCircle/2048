import os

import htmlmin
import lesscpy
from jinja2 import Environment, PackageLoader, select_autoescape
from jsmin import jsmin

if __name__ == "__main__":
    env = Environment(
        loader=PackageLoader("generate", "."),
        autoescape=select_autoescape(["html", "xml"]),
    )
    paths = [
        "bind_polyfill.js",
        "classlist_polyfill.js",
        "animframe_polyfill.js",
        "keyboard_input_manager.js",
        "html_actuator.js",
        "grid.js",
        "tile.js",
        "local_storage_manager.js",
        "game_manager.js",
        "application.js",
    ]
    scripts = []
    for filename in paths:
        with open(os.path.join("js", filename)) as file:
            scripts.append(jsmin(file.read()).replace("\n", ";"))
    min_script = ";".join(scripts)

    with open(os.path.join("style", "main.css")) as file:
        min_css = lesscpy.compile(file, minify=True, xminify=True)

    template = env.get_template("index.html.j2")
    min_html = htmlmin.minify(template.render(css=min_css, script=min_script))

    if not os.path.exists("dist"):
        os.makedirs("dist")
    with open(os.path.join("dist", "2048.html.w30"), "w") as file:
        file.write(min_html)
