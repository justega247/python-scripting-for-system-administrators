
# The ideal usage of the hr command is this:

    $ hr path/to/inventory.json
    Adding user 'kevin'
    Added user 'kevin'
    Updating user 'lisa'
    Updated user 'lisa'
    Removing user 'alex'
    Removed user 'alex'

# The alternative usage of the CLI will be to pass a --export flag like so:

    $ hr --export path/to/inventory.json

# This --export flag won’t take any arguments. Instead, you’ll want to default the value of this field to False and set the value to True if the flag is present. Look at the action documentation to determine how you should go about doing this.
#
# For this exercise, Write a few tests before implementing a CLI parser. Ensure the following:
#
#     An error is raised if no arguments are passed to the parser.
#     No error is raised if a path is given as an argument.
#     The export value is set to True if the --export flag is given.

# SOLUTION


# Here are some example tests:
#
# tests/test_cli.py

    import pytest

    from hr import cli

    @pytest.fixture()
    def parser():
        return cli.create_parser()

    def test_parser_fails_without_arguments(parser):
        """
        Without a path, the parser should exit with an error.
        """
        with pytest.raises(SystemExit):
            parser.parse_args([])

    def test_parser_succeeds_with_a_path(parser):
        """
        With a path, the parser should exit with an error.
        """
        args = parser.parse_args(['/some/path'])
        assert args.path == '/some/path'

    def test_parser_export_flag(parser):
        """
        The `export` value should default to False, but set
        to True when passed to the parser.
        """
        args = parser.parse_args(['/some/path'])
        assert args.export == False

        args = parser.parse_args(['--export', '/some/path'])
        assert args.export == True

# Here’s an example implementation for this cli module:
#
# src/hr/cli.py

    import argparse

    def create_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument('path', help='the path to the inventory file (JSON)')
        parser.add_argument('--export', action='store_true', help='export current settings to inventory file')
        return parser

