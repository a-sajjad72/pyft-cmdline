import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import platform
from PyInstaller.__main__ import run as run_pyinstaller

OS_NAME, MACHINE, ARCH = (
    sys.platform,
    platform.machine().lower(),
    platform.architecture()[0][:2],
)
if MACHINE in ("x86", "x86_64", "amd64", "i386", "i686"):
    MACHINE = "x86" if ARCH == "32" else ""


def main():
    opts, version = parse_options(), read_version()

    onedir = "--onedir" in opts or "-D" in opts
    if not onedir and "-F" not in opts and "--onefile" not in opts:
        opts.append("--onefile")

    name, final_file = exe(onedir)
    print(
        f"Building pyft-cmdline v{version} for {OS_NAME} {platform.machine()} with options {opts}"
    )
    print('Remember to update the version using "update-version.py"')
    print(f"Destination: {final_file}\n")

    opts = [
        f"--name={name}",
        *opts,
        "options.py",
    ]

    print(f"Running PyInstaller with {opts}")
    run_pyinstaller(opts)
    set_version_info(final_file, version)


def parse_options():
    # Compatibility with older arguments
    opts = sys.argv[1:]
    if opts[0:1] in (["32"], ["64"]):
        if ARCH != opts[0]:
            raise Exception(
                f"{opts[0]}bit executable cannot be built on a {ARCH}bit system"
            )
        opts = opts[1:]
    return opts


def exe(onedir):
    """@returns (name, path)"""
    name = "_".join(
        filter(
            None,
            (
                "pyft-cmdline",
                {"win32": "", "darwin": "macos"}.get(OS_NAME, OS_NAME),
                MACHINE,
            ),
        )
    )
    return name, "".join(
        filter(
            None, ("dist/", onedir and f"{name}/", name, OS_NAME == "win32" and ".exe")
        )
    )


def read_file(fname):
    with open(fname, encoding="utf-8") as f:
        return f.read()


def read_version(fname="version.py", varname="__version__"):
    """Get the version without importing the package"""
    items = {}
    exec(compile(read_file(fname), fname, "exec"), items)
    return items[varname]


def version_to_list(version):
    version_list = version.split(".")
    return list(map(int, version_list)) + [0] * (4 - len(version_list))


def set_version_info(exe, version):
    if OS_NAME == "win32":
        windows_set_version(exe, version)


def windows_set_version(exe, version):
    from PyInstaller.utils.win32.versioninfo import (
        FixedFileInfo,
        StringFileInfo,
        StringStruct,
        StringTable,
        VarFileInfo,
        VarStruct,
        VSVersionInfo,
    )

    try:
        from PyInstaller.utils.win32.versioninfo import SetVersion
    except ImportError:  # Pyinstaller >= 5.8
        from PyInstaller.utils.win32.versioninfo import (
            write_version_info_to_executable as SetVersion,
        )

    version_list = version_to_list(version)
    suffix = MACHINE and f"_{MACHINE}"
    SetVersion(
        exe,
        VSVersionInfo(
            ffi=FixedFileInfo(
                filevers=version_list,
                prodvers=version_list,
                mask=0x3F,
                flags=0x0,
                OS=0x4,
                fileType=0x1,
                subtype=0x0,
                date=(0, 0),
            ),
            kids=[
                StringFileInfo(
                    [
                        StringTable(
                            "040904B0",
                            [
                                StringStruct(
                                    "Comments",
                                    "pyft-cmdline%s Command Line Interface" % suffix,
                                ),
                                StringStruct(
                                    "CompanyName", "https://github.com/a-sajjad72"
                                ),
                                StringStruct(
                                    "FileDescription",
                                    "pyft-cmdline%s" % (MACHINE and f" ({MACHINE})"),
                                ),
                                StringStruct("FileVersion", version),
                                StringStruct("InternalName", f"pyft-cmdline{suffix}"),
                                StringStruct(
                                    "LegalCopyright", "Sajjad Ali | UNLICENSE"
                                ),
                                StringStruct(
                                    "OriginalFilename", f"pyft-cmdline{suffix}.exe"
                                ),
                                StringStruct("ProductName", f"pyft-cmdline{suffix}"),
                                StringStruct(
                                    "ProductVersion",
                                    f"{version}{suffix} on Python {platform.python_version()}",
                                ),
                            ],
                        )
                    ]
                ),
                VarFileInfo([VarStruct("Translation", [0, 1200])]),
            ],
        ),
    )


if __name__ == "__main__":
    main()