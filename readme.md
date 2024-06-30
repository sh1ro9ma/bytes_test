# bytesTest

## CPythonの用意

仮想環境を作成する

    pipenv --python 2.7.11

## ライブラリの追加

pytest環境

    pipenv install pytest

        Name: pytest
        Version: 4.6.11
        Summary: pytest: simple powerful testing with Python
        Home-page: https://docs.pytest.org/en/latest/
        Author: Holger Krekel, Bruno Oliveira, Ronny Pfannschmidt, Floris Bruynooghe, Brianna Laugher, Florian Bruhin and others
        Author-email: None
        License: MIT license
        Location: d:\work\14bytestest\.venv\lib\site-packages
        Requires: wcwidth, pathlib2, six, more-itertools, attrs, funcsigs, py, pluggy, colorama, atomicwrites, packaging, importlib-metadata
        Required-by: pytest-metadata, pytest-html

    pipenv install pytest-html

        Name: pytest-html
        Version: 1.22.1
        Summary: pytest plugin for generating HTML reports
        Home-page: https://github.com/pytest-dev/pytest-html
        Author: Dave Hunt
        Author-email: dhunt@mozilla.com
        License: Mozilla Public License 2.0 (MPL 2.0)
        Location: d:\work\14bytestest\.venv\lib\site-packages
        Requires: pytest, pytest-metadata
        Required-by:
