# jetson-sample


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


