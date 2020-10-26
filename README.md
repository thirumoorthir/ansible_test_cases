# Infrastructure Admin

## Creating and deploying admin keys

```bash
ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_devops_ed25519 -C "devops@zondax.ch"
```

Before starting the playbook, don't forget to install the public key of your master server on slaves servers, otherwise you will not be able to use it.

```bash
ssh-copy-id -i ~/.ssh/id_devops_ed25519 user@host
```

### Inventory and public keys

- Define host configuration at `config/hosts.yaml`

    > Tip: There is a template at `config_example/hosts.yaml`

    ```yaml
    all:
    vars:
        ansible_python_interpreter: auto

    hosts:
        hostABC:
        ansible_ssh_host: 1.2.3.4
        user_list:
            - user1
        sudoer_list:
            - user2
        user_zsh_list:
            - user3

        hostXYZ:
        ansible_ssh_host: 5.6.7.8
        user_list:
            - user1
        user_zsh_list:
            - user3
    ```

- Considering adding these hosts to groups

    ```yaml
    [base]
    hostABC
    hostBCD

    [docker]
    hostXYZ
    ```

- Copy SSH pub keys for each users you want to create  `config/{USERNAME}.pub`

## Running Tests

- First install dependencies

    ```shell
    make install_dependencies
    ```

- To run tests use

    ```shell
    make test
    ```


## Running Playbooks

- To check all files are valid

    ```bash
    make check
    ```


- To check node connections

    ```bash
    make check_nodes
    ```

- Basic configuration

    ```bash
    make base
    ```

- Configure everything

    ```bash
    make configure
    ```
