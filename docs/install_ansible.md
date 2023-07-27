# install_ansible

本ドキュメントは、ansibleに関する簡単な概要とセットアップ手順について記します。
ansibleに関する詳しい情報は、公式ドキュメントを参照してください。

- https://docs.ansible.com/ansible/2.9_ja/installation_guide/intro_installation.html

# ベストプラクティス

ansibleプロジェクトを構成する際のベストプラクティスについては、以下のドキュメントを参照してください。

- https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html


# コントロールノードのセットアップ

コントロールノードは、構築対象となるホストの管理と、管理ホストに対して構築を行うノードです。


ansible をインストールします。

- https://docs.ansible.com/ansible/2.9_ja/installation_guide/intro_installation.html#ubuntu-ansible

```
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```

対象ホスト（`your_host`）に対して疎通確認を行う。

``` 
# ansibleにおけるpingは、「ssh接続を行い、Pythonが実行可能」であるかの検証を行う
ansible -i 'your_host,' -m ping all
```

バージョンを確認する。

```
ansible --version
```

# インベントリーの管理

インベントリーとは、管理対象のホストをグループ化したもの。

インベントリーはデフォルトで`/etc/ansible/hosts`を参照する。


hosts.ymlを作成する。

```
---
iot-devices:
  hosts:
    jetson-1
```



```
ansible -i hosts.yml -m ping iot-devices
```


playbookを実行する。
実行対象ホストは、echo_hello.yml の定義に依存します。

`echo_hello.yml`は、`all`としているため全ての管理ホストに対して実行されます。

```
ansible-playbook -i hosts.yml playbooks/echo_hello.yml
```

任意のグループ、ホストを対象のみを対象としたい場合、`--limit`オプションを使用できます。

```
ansible-playbook -i hosts.yml playbooks/echo_hello.yml --limit target_host_or_group
```



# 設定

ansible は Python を使用する。

デフォルトではグローバルインタープリター（`/usr/bin/python` など）を参照する。


また、ターゲットマシン上でも Python を使用する。

ターゲットマシン上で実行するPythonインタープリターは、`/etc/ansible/hosts`で指定する。

