# setup_jetson


# セットアップ

詳細な手順は公式サイト参照。

- https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#prepare


手順の概要は次の通り。

- MicroSD にJetson のモデル（Nano や Xavier など）に合ったイメージを焼く
- キーボード、マウス、ディスプレイ、Lanケーブルを繋ぐ
- DC電源(5V/2A)を繋ぐとセットアップが始まる
  - DC電源を使うとヘッドレスで設定が可能
  - MicroUSBを電源として使えるが、その場合ヘッドレスは不可
  - ヘッドレスモードの設定の際に、MicroUSB を通信用として使用する


## 詳細セットアップ

- セットアップ時に日本語キーボードをインストールする
- 上記だけではローマ字に入力がまだできない。テキスト入力で日本語（mozc bus）を追加する
- ssh 接続して使う場合は不要か？


# ストレージについて

Jetson のモデルによってストレージの構成が異なる。

- Nano は microSD
- TX2 や Xavier は内部に eMMC ストレージを備える


# 初期環境構築

```
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
```


- docker はインストール済み
	- 作成したユーザーはdocker グループに属していないので `sudo usermod -aG docker $USER` する
	- グループ反映は設定後再ログインする
	- /etc/docker/daemon.json に nvidia runtime は設定済み
		- "default-runtime": "nvidia" とすると、デフォルトでgpuを使う（gpus=オプションを指定することでnvidia runtimeが使用される）
		- 通常は runc がデフォルトランタイム


# docker の使用

Jetson は arm アーキテクチャなので arm 用にビルドされたイメージが必要。

Jetson 用のベースイメージはここから見つけることができる。

https://catalog.ngc.nvidia.com/orgs/nvidia/containers/l4t-ml


なお、JetPack のバージョンに合うイメージを使用する。



# 情報収集

l4t のバージョン確認は次の通り。

```
cat /etc/nv_tegra_release
dpkg-query --show nvidia-l4t-core

# R32 (release), REVISION: 7.1, GCID: 29818004, BOARD: t210ref, EABI: aarch64, DATE: Sat Feb 19 17:05:08 UTC 2022
# nvidia-l4t-core 32.7.1-20220219090432
```

```
docker run --rm --gpus=all -it nvcr.io/nvidia/l4t-ml:r32.7.1-py3 python3 -c "import sys;print('Python ' + sys.version);import torch;print(torch.cuda.is_available());print(torch.cuda.device_count())"

# True
# 1
```

上記のイメージは11GBある。
ストレージは最低32GBは用意した方がいいだろう。



リアルタイムにパフォーマンスを計測するなら

```
tegrastats
```


アーキテクチャ情報を取得

```
uname -m

# x86_64: 64ビットのx86
# armv7l: 32ビットのarm
# aarch64: 64ビットのarm
```

これも

```
lscpu
```


