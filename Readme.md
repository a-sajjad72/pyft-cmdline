# pyft-cmdline

pyft-cmdline is a command line version of [pyft](https://github.com/a-sajjad72/pyft) (a python based file transfer framework)

## Table of contents

- [INSTALLATION](#installation)
- [BUILD FROM SOURCE](#build-from-source)
  - [Pre-requisites](#pre-requisites)
  - [Cloning the repository](#cloning-the-repository)
  - [Setting up virtual environment](#setting-up-vrtual-enviromnent)
  - [Installing dependencies](#installing-dependencies)
  - [Building release](#building-release)
- [USAGE AND OPTIONS](#usage-and-options)
  - [send subcommand](#send-subcommand)
  - [recv subcommand](#recv-subcommand)
  - [Examples](#examples)
- [CONTRIBUTING](#contributing)
  - [Issues and Bug Reports](#issues-and-bug-reports)
  - [Feature Requests](#feature-requests)
  - [Pull Requests](#pull-requests)
  - [Code Style and Conventions](#code-style-and-conventions)

## INSTALLATION

You can install pyft-cmdline using the below release files

| File                     | Description                            |
| :----------------------- | :------------------------------------- |
| [pyft-cmdline.exe]()     | Windows standalone x64 binary          |
| [pyft-cmdline_x86.exe]() | Windows standalone x86 (32-bit) binary |

**_NOTE:_** Currently only windows releases are available. You can build it for your OS. It's really easy. See the section below about [building from source](#build-from-source)

## BUILD FROM SOURCE

If want to build pyft-cmdline by your own one thing to be noted that the library we use to build pyft-cmdline does not support cross-compilation i.e you can't build pyft-cmdline for Linux and MacOS on Windows and vice versa.

### Pre-requisites

- You must have [Python 3.10](https://www.python.org/downloads/release/python-31011/) or above and [git](https://git-scm.com/) added to your Path

### Cloning the repository

It's recommended to clone the repository because the framework which is used by pyft-cmdline is added as a submodule in the repository.

Clone the repository and its submodule at the same using `--recurse-submodules` option:

```
git clone https://github.com/a-sajjad72/pyft-cmdline.git --recurse-submodules
```

If you've already cloned the repo then run this command from the repo root to make sure you have the latest changes of the submodules to your code:

```
git submodule update --init --recursive
```

### Setting up Virtual Enviromnent

Before building we need to setup the envrionment. It's recommended to use Python virtual environment before starting work with projects.

head up to the root of your cloned repo and run the following commands one by one

```
python -m venv venv
.\venv\Scripts\activate
```

### Installing dependencies

Here are some of the dependencies that we need to build pyft-cmdline.

```
python -m pip install -r requirements.txt
```

### Building release

**_NOTE:_** We are using [Pyinstaller](https://github.com/pyinstaller/pyinstaller) to build release for our platform. The thing to noted is that Pyinstaller doesn't support cross-compilation which means that we can't build a release for Linux or MacOS on Windows and vice versa.

```
python -m pyinstaller options.py -n pyft-cmdline --onefile
```

After executing the above command wait for a while and you'll get your standalone executable in the `dist` folder in the root of your repo.

## USAGE AND OPTIONS

Here are some the pyft-cmdline commands with their usage.

```
usage: pyft-cmdline.exe [-h] [-V] [-U] {send,recv} ...

options:
  -h, --help     show this help message and exit
  -V, --version  show program's version number and exit
  -U, --update   Update pyft-cmdline.exe to the latest version

subcommands:
  Available subcommands

  {send,recv}
    send         Send a file
    recv         Receive files

To read about or get help with a specific subcommand, use 'pyft-cmdline.exe <subcommand> --help'.
```

### send subcommand

```
usage: pyft-cmdline.exe send [-h] --address ADDRESS FILE [FILE ...]

positional arguments:
  FILE               Path(s) to the file(s) you want to send

options:
  -h, --help         show this help message and exit
  --address ADDRESS  Address of the receiver. [Required]
```

### recv subcommand

```
usage: pyft-cmdline.exe recv [-h] [-P PATH]

options:
  -h, --help            show this help message and exit
  -P PATH, --path PATH  Use custom directory path to save
                        received files. Default to current
                        working directory
```

### Examples

Opt one of the below way to work with pyft-cmdline.

- Open your favorite terminal and change your directory to the where you put pyft-cmdline.

- On Windows, `Shift+Right-click` on the empty area of the direcoty where you put pyft-cmdline and select `open powershell window here`

Yeah nothing is more explanatory than examples. here are some examples which shows the use of above options.

#### Receive files

Store the receive files in the current working tree.

```
pyft-cmdline.exe recv
```

Store the receive files to the path specified

```
pyft-cmdline.exe recv -P path/to/store/received/files
```

**_Note:_** After executing the above commands an address is shown in the terminal. this address is needed by sender to send files to you.

#### Send files

Sends the file to the `ADDRESS` (shown on the receiver's terminal)

```
pyft-cmdline.exe send path/to/file --address ADDRESS
```

Send the files to the `ADDRESS`

```
pyft-cmdline.exe send file1 file2 file3 ... --address ADDRESS
```

**_NOTE:_** If the filename(s)/filepath(s) contain spaces then enclosed the filenames(s)/filepath(s) in **double quotes (")**.

## CONTRIBUTING

Thank you for considering contributing to this command line utility! We appreciate your interest in making this project better. By contributing, you can help improve its functionality, add new features, fix bugs, and enhance the overall user experience.

To ensure a smooth and efficient collaboration, please follow these guidelines when contributing to the project:

### Issues and Bug Reports

If you encounter any issues or bugs while using the utility, please check the existing issues on the GitHub repository to see if the problem has already been reported. If not, you can create a new issue with a detailed description of the problem, steps to reproduce it, and any relevant error messages. We'll review the issue and respond as soon as possible.

### Feature Requests

We welcome suggestions for new features or enhancements to the utility. If you have an idea that could benefit the project, please create a new issue on the GitHub repository and provide a clear description of the feature request. We'll evaluate the suggestion and discuss it with the community.

### Pull Requests

If you would like to contribute code to the project, you can do so by submitting a pull request. Here's how:

1.  Fork the repository to your GitHub account.
2.  Create a new branch for your changes: `git checkout -b my-feature`.
3.  Make the necessary modifications and ensure the code follows the project's coding style and conventions.
4.  Write tests to cover the changes you've made, if applicable.
5.  Commit your changes with a descriptive commit message: git commit -m "Add my feature".
6.  Push your branch to your forked repository: git push origin my-feature.
7.  Open a pull request on the main repository, describing your changes and their purpose.

### Code Style and Conventions

Maintaining a consistent code style throughout the project helps keep the codebase clean and readable. Please adhere to the following guidelines when contributing:

Follow the existing code formatting and indentation patterns.

- Use descriptive variable and function names.
- Include inline comments when necessary to clarify complex logic.
- Ensure your code passes any existing unit tests and write new tests for your changes whenever possible.
