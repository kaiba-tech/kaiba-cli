import subprocess


def test_atleast_two_arguments_needed_none():
    """Test that we must supply 2 arguments, and errors when none."""
    cli_result = subprocess.run(
        ['piri'],
        capture_output=True,
    )
    assert b'the following arguments are required: config' in cli_result.stderr
    assert cli_result.returncode == 2


def test_atleast_two_arguments_needed_one():
    """Test that we get file not found error when bad file."""
    cli_result = subprocess.run(
        ['piri', 'config.js'],
        capture_output=True,
    )
    assert b'the following arguments are required: input' in cli_result.stderr
    assert cli_result.returncode == 2


def test_bad_config_file_path_or_name():
    """Test that we get file not found error when bad file."""
    cli_result = subprocess.run(
        ['piri', 'config.js', 'input.json'],
        capture_output=True,
    )
    assert b'FileNotFoundError' in cli_result.stderr
    assert b'config.js' in cli_result.stderr


def test_running_ok():
    """Test that we can map ok."""
    cli_result = subprocess.run(
        ['piri', 'tests/files/good_config.json', 'tests/files/input.json'],
        capture_output=True,
    )
    assert cli_result.returncode == 0


def test_running_with_badly_formatted_config():
    """Test that badly formatted config yields error message."""
    cli_result = subprocess.run(
        ['piri', 'tests/files/bad_config.json', 'tests/files/input.json'],
        capture_output=True,
    )
    assert b"'target' is a required property" in cli_result.stderr
