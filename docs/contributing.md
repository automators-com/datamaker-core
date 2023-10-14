# Contributing

## Pre-requisites

- [Python3](https://www.python.org/downloads/)
- [hatch](https://hatch.pypa.io/latest/)
- [pipx](https://pipxproject.github.io/pipx/) (optional)

## Setup

The following steps can be followed to set up a development environment.

1. Clone the project and enter into the directory:

    ```sh
    git clone https://github.com/automators-com/datamaker-core.git
    cd datamaker-core
    ```

2. Install [hatch](https://hatch.pypa.io/latest/)

    ```sh
    pip install hatch
    ```

    or preferably:

    ```sh
    pipx install hatch
    ```

3. Enter the default environment (this will activate the default virtual environment and install the project in editable mode).

    ```sh
    hatch shell default
    ```

You can now proceed to make changes to the project.

## Environments

This project uses [hatch](https://hatch.pypa.io/latest/) to manage virtual environments. The following environments are available:

- `default` - This is the default environment and is used for development purposes.
- `docs` - This environment is used to build the documentation.
- `test` - This environment is used to run the tests.

More details around the various environments can be found in the `pyproject.toml` file.

## Testing

This project uses `pytest` for testing purposes. The tests can be found in the `tests` directory. Tests will run after every commit (locally) and on every push (using github actions) but can also be run manually using:

```sh
hatch run test
```

## Linting

This project is linted using `ruff` and formatted with `black`. The linting and formatting can be run manually using:

```sh
hatch run lint
```

```sh
hatch run format
```

## Building the package

The package can be built using:

```sh
hatch run build
```

## Documentation

The documentation for this project can be found in the `docs` directory. The documentation is created using mkdocs and can be viewed locally using:

```sh
hatch run docs:serve
```

The docs can also be built for deployment using:

```sh
hatch run docs:build
```
