import re


def test_version(host):
    version = host.check_output('fd --version')
    pattern = r'fd [0-9\.]+'
    assert re.search(pattern, version)
