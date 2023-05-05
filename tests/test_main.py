from typer.testing import CliRunner

from iris_cli.main import app

runner = CliRunner()


def test_ping():
    result = runner.invoke(app, ["ping"])
    assert result.exit_code == 0
    assert "pong" in result.stdout
    assert "pong\n" == result.stdout


def test_post_get_predict():
    result = runner.invoke(app, ["post-get-predict", '0', '0', '0', '0'])
    assert result.exit_code == 0
    assert "{'flower_class': 'Iris Setosa'}\n" == result.stdout





