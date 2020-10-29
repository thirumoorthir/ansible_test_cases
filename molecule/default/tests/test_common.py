import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# Test to make sure the this is an ubuntu server
def test_os_release(host):
    assert host.file("/etc/os-release").contains("ubuntu")

# Test to make sure that this servers is running sshd service 
def test_sshd_inactive(host):
    assert host.service("sshd").is_running is True


# This is for make sure that these three users exits 
users = ["user1", "user2", "user3"]
def test_users_exits(host):
    user = host.user
    for x in users:
        assert user(x).exists
       # assert len(user(x).password) == 0 
    
#    host.user("user").exists

# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected


 