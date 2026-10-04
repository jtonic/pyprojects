# Plan: Enable Python Type Checking with `basedpyright`

**Context:** Chosen tool = `basedpyright`. Use `pipx`/`pip`/`venv` until migrating to `uv`. Primary editor = `Zed`. Adopt incrementally (gradual typing).

## Implementation

- [x] **1) Add dev dependencies**
  - Add `types-requests` to dev dependencies in `pyproject.toml` (e.g. `[project.optional-dependencies] dev = ["types-requests"]`). `basedpyright` will be installed via `pipx` (not as a project dependency).
  - _How to test:_ `basedpyright --version` runs after `pipx install basedpyright`. `pip show types-requests` shows it installed after `pip install -e .[dev]`.

- [x] **2) Configure `basedpyright`**
  - Add minimal config to `pyproject.toml` under `[tool.basedpyright]` (e.g. `pythonVersion = "3.14"`, `typeCheckingMode = "basic"` or `standard`, avoid strict globally).
  - _How to test:_ Run `basedpyright .` from repo root; it loads config and reports no config errors.

- [x] **3) Verify dependency type availability**
  - Confirm `click` 8.x has inline types (no `types-click` needed). Keep `types-requests` for requests. If others appear untyped, leave as `Any` (do not force stubs).
  - _How to test:_ Run `basedpyright .` and confirm no missing-stub noise from existing deps under chosen mode.

- [x] **4) Add simple addition function and verify basedpyright**
  - Created `mycli/type_checked_test.py` with `add(a: int, b: int) -> int` returning `str(result)` to intentionally trigger a type error; verified `basedpyright mycli/type_checked_test.py` reports: error "Type 'str' is not assignable to return type 'int'" (reportReturnType).
  - Added `# type: ignore[return-value]` to suppress the error and verified basedpyright reports 0 errors. Kept the file in place for manual testing in Zed.
  - _How to test:_ Run `basedpyright mycli/type_checked_test.py` — with ignore it passes; without ignore it fails as expected.

- [ ] **5) Annotate core CLI surface incrementally**
  - Typed the entry point and key commands: `mycli/cli.py` (`main() -> None`), `mycli/commands/users.py` (`add(name: str, age: int, gender: str) -> None`, `Gender` enum as-is, `click.Choice` on values for UX).
  - Used `# type: ignore[return-value]` only in `mycli/type_checked_test.py` for intentional mismatch testing.
  - _How to test:_ `basedpyright mycli/cli.py mycli/commands/users.py` passes with 0 errors.

- [ ] **6) Verify Zed integration** (manual)
  - Open the project in `Zed` and confirm `basedpyright` LSP reports feedback on annotated code without flooding errors from untyped modules/deps.
  - _How to test:_ Edit an annotated function in Zed and confirm real-time diagnostics appear as expected. (e.g. remove/add ignore in `mycli/type_checked_test.py` to see diagnostics).

## Final test

Use this as the validation checklist for both the developer (human) and the AI agent:

1. **Environment**: Create/activate a venv (`python -m venv .venv && source .venv/bin/activate`) using `pip`/`venv` (no `uv`).
2. **Install tools**: Install `basedpyright` via `pipx` (`pipx install basedpyright`). Install project dev deps (`pip install -e .[dev]`) to get `types-requests`.
3. **Type check**: Run `basedpyright .` from repo root. **Pass criteria:** exit code 0 and no new type errors introduced by this change (pre-existing untyped code may remain fine under the chosen mode).
4. **Editor check**: In Zed, open `mycli/cli.py` and verify real-time `basedpyright` diagnostics are correct (no global red flood from untyped deps).
5. **Sanity**: Run the CLI (`mycli --help`) to ensure runtime behavior is unchanged.

**Success:** All steps pass. Implementation is complete and ready for review.
