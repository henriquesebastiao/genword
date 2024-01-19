from typer.testing import CliRunner

from genword.cli import __version__, app

runner = CliRunner()


def test_cli_return_0_to_stdout():
    result = runner.invoke(app, ['a', '1', '1'])
    assert result.exit_code == 0


def test_cli_version_command():
    result = runner.invoke(app, ['--version'])
    assert __version__ in result.output


def test_cli_verbose_command():
    result = runner.invoke(app, ['ab', '2', '2', '--verbose'])
    for word in ['aa', 'ab', 'ba', 'bb']:
        assert word in result.output
