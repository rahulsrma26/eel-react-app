"""Python test eel application with react for UI"""

import argparse
import json
import os

import eel
import app.backend  # this will include exposed functions


def get_args():
    parser = argparse.ArgumentParser(
        prog=os.path.basename(__file__),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
    )
    parser.add_argument(
        "-d",
        "--dev",
        action="store_true",
        help="development in browser instead of separate window",
    )
    parser.add_argument(
        "-c", "--config", type=str, default="", help="config file (search for config.json if empty)"
    )
    return parser.parse_args()


def main(args):
    if not args.config:
        if os.path.isfile('config.json'):
            args.config = 'config.json'
        elif os.path.isdir('public'):
            args.config = 'public/config.json'
        else:
            args.config = '../public/config.json'

    with open(args.config, 'r') as f:
        config = json.load(f)

    if args.dev:
        web_dir = "src"
        app = None
        page = {"port": config['vite']['port']}
        exts = [".tsx", ".ts", ".jsx", ".js", ".html"]
        print(f"Local: http://{config['app']['host']}:{config['vite']['port']}")
    else:
        web_dir = "dist"
        app = "chrome"
        page = "index.html"
        exts = [".js", ".html"]

    base_dir = os.path.dirname(__file__)
    eel.init(os.path.join(base_dir, web_dir), allowed_extensions=exts)

    eel_kwargs = dict(
        host=config['app']['host'],
        port=config['app']['port'],
        size=(800, 600),
    )
    eel.start(page, mode=app, **eel_kwargs)


if __name__ == "__main__":
    main(get_args())
