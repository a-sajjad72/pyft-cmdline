import recieve as receiver
import send as sender
import argparse
import pathlib
import os
from sys import exit

__version__ = "2023.7.23"

if __name__ == "__main__":
    # Create the main parser
    parser = argparse.ArgumentParser(
        prog="pyft-cmdline.exe",
        epilog="To read about or get help with a specific subcommand, use '%(prog)s <subcommand> --help'.",
    )

    parser.add_argument("-V", "--version", action="version", version=f"{__version__}")

    # Create subparsers for send and receive
    subparsers = parser.add_subparsers(dest="subcommand", description="Available subcommands"
    )

    # Create the parser for the "send" subcommand
    send_parser = subparsers.add_parser("send", help="Send a file")
    send_parser.add_argument(
        "file",
        nargs="+",
        type=pathlib.Path,
        metavar="FILE",
        help="Path(s) to the file(s) you want to send",
    )
    send_parser.add_argument(
        "--address", type=str, required=True, help="Address of the receiver \"ip:[port]\". if port not specified it default to 9999"
    )
    # Create the parser for the "receive" subcommand
    receive_parser = subparsers.add_parser("recv", help="Receive files")
    receive_parser.add_argument(
        "-P",
        "--path",
        action="store",
        type=pathlib.Path,
        help="Use custom directory path to save received files. Default to current working directory",
    )

    # Parse the command line arguments
    args = parser.parse_args()

    # Accessing the subcommand and arguments
    if args.subcommand == "send":
        ip, port = args.address.split(":") if ':' in args.address else (args.address,None)
        # checking provided path(s) is valid
        for x in args.file:
            if os.path.exists(str(x)):
                if not os.path.isfile(str(x)):
                    print(
                        f'ERROR: "{x}" is not a file.\n Directories are not currenlty supported'
                    )
            else:
                print(f'ERROR: "{x}" not exists')
                exit()

        if port is None:
            sender.Sender(ip, 9999, args.file)
        else:
            sender.Sender(ip,  int(port), args.file)
        exit()

    elif args.subcommand == "recv":
        if args.path:
            receiver.Reciever(path=args.path)
        else:
            receiver.Reciever()
        exit()

    else:
        # No subcommand provided
        print("Please provide a subcommand (send/receive)\n")
        parser.print_help()
