check:
	@ansible-playbook -i config/hosts.yaml configure.yml --syntax-check

check_nodes:
	@ansible -i config/hosts.yaml all -m ping -u root

basic:
	@ansible-playbook -i config/hosts.yaml basic.yml

debug:
	@ansible-playbook -i config/hosts.yaml debug.yml

configure:
	@ansible-playbook -i config/hosts.yaml configure.yml

install_dependencies:
	pip install -U ansible molecule molecule-docker yamllint ansible-lint ruamel.yaml

MOLECULE_DISTRO ?= ubuntu2004

test:
	yamllint .
	ansible-lint
	MOLECULE_DISTRO=$(MOLECULE_DISTRO) molecule test
