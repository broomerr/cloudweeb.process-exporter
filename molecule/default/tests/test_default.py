import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config_file(host):
    f = host.file('/etc/process_exporter.yml')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_socket(host):
    s = host.socket("tcp://127.0.0.1:9256")
    assert s.is_listening
