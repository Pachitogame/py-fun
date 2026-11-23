# Assignment B · Python project setup

## Run and inspect the project

Use Python 3.12 or later and GNU Make. From the extracted project directory:

```sh
python -m venv .venv
. .venv/bin/activate
make install
make run
make build
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. The supplied dev container provides Python and Make. The build runs the tests, writes the source distribution to `dist/`, and generates the API reference at `dist/html/index.html`. The demonstration output is in `results.txt`.

## Project setup

1. **Project scaffold.** The scaffold is the starting layout. Here, `main.py` launches the demonstrations, `src/` holds both components, and `tests/` mirrors them. The build rules and dependency list live at the root. This gives someone changing the calculator a predictable place to find its tests.
2. **Build process.** A build is a repeatable sequence that turns a particular source revision into a distributable artifact and checks that the artifact's inputs work together.
3. **Start and end.** The process starts with a selected source revision and its build configuration. It ends when the required checks pass and the distribution is generated. Deployment happens separately.
4. **Steps and result.** Install the development dependencies, run the unit tests, package a source distribution and generate documentation. For this project, the package is `dist/py_fun-1.0.0.tar.gz`.
5. **Make.** GNU Make reads targets, prerequisites and recipes from a Makefile. For example, `make package` runs its prerequisite `tests` before executing the packaging recipe. A failing test stops that build.
6. **requirements.txt.** This file lists packages pip should install into the active environment. Here it includes pytest, Sphinx and the build frontend. Run `python -m pip install -r requirements.txt` or `make install`.
7. **Build server.** A build server checks out a revision into a controlled environment and executes the build automatically. For Python it selects an interpreter, installs dependencies, runs tests and archives distributions and logs.
8. **Nightly build.** A scheduled build runs against a chosen branch each night. Its test results can reveal integration problems introduced by changes made during the day.
9. **Script, module, package and library.** Running `python main.py` uses the file as a script. An importable file such as `calculator.py` is a module. A package such as `src.calculator` groups modules under a common import name. A library is reusable functionality that may span multiple modules or packages.
10. **__init__.py.** Python executes this file on the first import of a regular package in a process. Here it exposes public names, so tests can write `from src import Calculator`. Namespace packages can omit it.

Reading: Kenneth Reitz, [Structuring Your Project](https://docs.python-guide.org/writing/structure/).

## Development container

1. **Program location.** A shell searches the directories in its PATH. Debian's make package installs the executable as `/usr/bin/make`. Run `command -v make` and `make --version` inside the rebuilt container to check.
2. **Rebuilding.** A manual apt installation affects the running container's writable layer. Recreating the container from the original image loses that installation.
3. **Persistent installation.** Put the apt installation in the image recipe and rebuild. The modified Dockerfile installs Git and GNU Make together and removes the apt index afterwards.
4. **Dockerfile purpose.** The dev-container configuration selects the Dockerfile to build the Python development image used by VS Code.
5. **Instructions.** FROM selects the Python 3.12 slim base image. ENV sets persistent environment defaults for Python. WORKDIR selects /workspace as the default working directory. RUN executes a build-time shell command and commits its filesystem changes into the image.

## Why did adding two strings produce 11?

Python defines `+` between two strings as concatenation. The original operands were each the character “1”, so the result was the two-character string “11”. The calculator now converts both operands before arithmetic. For example, `add("1", "1")` gives the integer 2 and `add("three", "1.600")` gives 4.6. The supplied tests define the fallback for an unknown operand as zero and the result of division by zero as positive infinity.

## Git and handoff

Use `git log --all --oneline --decorate --graph` to inspect the history. The main branch contains the application and the git-modules branch records the editor and container settings. The ZIP includes both submodule repositories and the local Dockerfile commit. In VS Code select **Dev Containers: Rebuild and Reopen in Container** to exercise that image, then run the tests in the Testing view.

For SSH publication, register your public key with your Git host and create an empty project repository. Publish the changed dev-container commit to a fork you control first, then on the git-modules branch update that submodule URL in .gitmodules to point to the fork and commit it. This lets a fresh clone resolve the new commit. Add your project’s SSH clone URL as origin, then run `git push -u origin main git-modules` and `git push origin --tags`.
