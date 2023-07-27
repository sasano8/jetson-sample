# jetson-sample


# aaa


```
# Iot向けのUbuntu20.04の仮想マシンを作成
multipass lanch core20
```



cat ~/.ssh/id_rsa.pub:q!


```
# 起動できる仮想マシンイメージの確認
multipass find

# 仮想マシンの起動
multipass launch 22.04

# 接続先を定める
TARGET_HOST=your_host
TARGET_USER=ubuntu

# 公開鍵の登録
cat ~/.ssh/id_rsa.pub | multipass transfer - $TARGET_HOST:/home/$TARGET_USER/pub_key
multipass exec $TARGET_HOST -- bash -c "cat /home/$TARGET_USER/pub_key >> /home/$TARGET_USER/.ssh/authorized_keys"
multipass exec $TARGET_HOST -- rm /home/$TARGET_USER/pub_key

# 起動した仮想マシンのipを確認
multipass list

```

`hosts.yml`に登録

```
iot-devices:
  hosts:
    worker-1:
      ansible_host: 10.28.186.xxx
      ansible_user: ubuntu
```


```
ansible-playbook -i hosts.yml --limit iot-devices playbooks/echo_hello.yml
```
