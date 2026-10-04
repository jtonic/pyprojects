< [back](../README.md)

# MyCLI

## How to intall run and build

```shell
mise install

mise exec -- python --version
mise exec -- pipx --version

python -m venv .venv

source .venv/bin/activate

# for development (editors & ide)
pip install -e . --force

# to install mycli to be globally available command with isolated and ephemeral virtual environment
pipx install -e . --force

# configure the zsh completion
echo 'eval "$(_MYCLI_COMPLETE=zsh_source mycli)"' >> ~/.zshrc
```

## Notes

- common editors / IDEs offers the support for python virtual envs (.venv)

This is how it looks in the Zed editor when python language support is triggered (a python file is opened)

Status bar

![zed_status_bar](companion/doc/assets/zed_status_bar.png)

And this is how it looks when by clicking on the status bar button the first suggestion is the best one (.venv)

![zed_python_envs_sugessions](companion/doc/assets/zed_python_envs_sugessions.png)

There are similar suggestions for other editors and IDEs such as VSCode, PyCharm, IntelliJ.
