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
