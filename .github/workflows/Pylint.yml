name: PyLint
on:
  push:
    paths:
    - "**.py"
  workflow_dispatch:
jobs:
  PEP8:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"
      - name: Install libraries
        run: pip install autopep8 autoflake isort black
      - name: Check for showstoppers
        run: |
          autopep8 --verbose --in-place --recursive --aggressive *.py
      - name: Remove unused imports
        run: |
          autoflake --in-place --recursive --remove-all-unused-imports --ignore-init-module-imports .

      - name: Lint with Isort 
        run: |
          isort .
      - name: Lint with Black
        run: |
          black .
      - uses: stefanzweifel/git-auto-commit-action@v4
        with:
            commit_message: "Auto Fixes"
            commit_options: "--no-verify"
            repository: .
            commit_user_name: "github-actions[bot]"
            commit_user_email: "41898282+github-actions[bot]@users.noreply.github.com"
            commit_author: "github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>"
