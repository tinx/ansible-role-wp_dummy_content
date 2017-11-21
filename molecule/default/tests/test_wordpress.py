import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_web_server_running(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening


def test_item_count(host):
    cmd = host.run_expect([0], "/tmp/verify.py")
    lines = cmd.stdout.splitlines()
    assert len(lines) == 4
    assert lines[0] == "post amount: 17"
    assert lines[1] == "post comments: 102"
    assert lines[2] == "page amount: 5"
    assert lines[3] == "page comments: 24"
    # Note: the last test should show 24 comments, not 30, because
    # the blog is initialized with one initial page that has comments
    # closed, so only the four new pages get 6 comments. Hence, 24.
