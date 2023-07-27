# 検証済みマトリクス


Ubuntu 20.04 以降はPythonが入っていないということだったが、入っているみたい

|  OS  |  result  |  memo  |
| ---- | ---- | ---- |
|  Ubuntu Core 22  | false  |  aptがない  |
|  Ubuntu 22  | true |    |



コントロールノードで以下を実行します。

```
sudo groupadd xdata_ansible
sudo usermod -aG xdata_ansible <user_name>
```
