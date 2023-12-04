import argparse

from busyauthor import __version__
from busyauthor import args_common as argsmod

parser = argparse.ArgumentParser(
    description="Just a command, sub command, subsub command demonstration"
)
argsmod.add_common_args(parser)


parser.add_argument(
    "--version",
    action="version",
    version=f"busyauthor {__version__}",
)
parser.add_argument("--db", help="Specify the database file (e.g., data.cypher)")


subparsers = parser.add_subparsers(
    description="valid commands",
    title="command",
    help="command help",
    required=True,
    dest="command",
)

command_parser = subparsers.add_parser(
    "command", aliases=["cmd"], help="Top-level command"
)
command_parser.add_argument("--command-args", help="Arguments for the command")
argsmod.add_common_args(command_parser)

subcommand_parser = command_parser.add_subparsers(
    dest="subcommand", help="Available subcommands"
)
subcommand_parser = subcommand_parser.add_parser(
    "subcommand", aliases=["subcmd"], help="Subcommand"
)
subcommand_parser.add_argument("--subcommand-args", help="Arguments for the subcommand")
argsmod.add_common_args(subcommand_parser)
