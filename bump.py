from bs4 import BeautifulSoup

import os
import sys
import shutil

def _get_app_name():
    app_name = sys.argv[1]
    allowed_app_names = []
    for item in os.listdir("."):
        if os.path.isdir(item) and not item.startswith("."):
            allowed_app_names.append(item)

    if app_name not in allowed_app_names:
        _init_package_page(app_name)

    return app_name

def _init_package_page(app_name):
    os.mkdir(app_name)
    shutil.copyfile("package-page-template.html", f"{app_name}/index.html")
    with open(f"{app_name}/index.html", "r+") as html:
        package_page = BeautifulSoup(html, 'html.parser')
        package_page.find("title").string = app_name

    with open(f"{app_name}/index.html", "w") as html:
        html.write(str(package_page.prettify()))

def _get_version_number():
    version_number = sys.argv[2]
    return version_number


def _get_protocol():
    protocol = sys.argv[3]

    allowed_protocols = ["https", "ssh"]
    if protocol not in allowed_protocols:
        print(f"This protocol is not supported. Please choose one in '{allowed_protocols}'.")
        exit(1)

    return protocol


if __name__ == "__main__":
    app = _get_app_name()
    version = _get_version_number()
    protocol = _get_protocol()

    with open("commit_message.txt", "w") as f:
        commit_message = f"Publish {app} - {version}"
        f.write(commit_message)

    with open(f"{app}/index.html", "r+") as html:
        soup = BeautifulSoup(html, 'html.parser')
        new_a = soup.new_tag("a")
        new_a["href"] = f"git+{protocol}://git@github.com/sampler-box/{app}.git@{version}#egg={app}-{version}"
        new_a.string = f"{app}-{version}"
        soup.html.body.insert(0, new_a)

    with open(f"{app}/index.html", "w") as html:
        html.write(str(soup.prettify()))

    sys.stdout.write(commit_message)