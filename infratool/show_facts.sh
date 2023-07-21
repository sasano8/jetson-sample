#!/bin/bash

# JSONファイルが保存されているディレクトリ
facts_dir="facts"

# jqコマンドで抽出するフィールド
fields="hostname: .hostname, os_family: .os_family, distribution: .distribution, distribution_version: .distribution_version, architecture: .architecture, memtotal_mb: .memtotal_mb, memfree_mb: .memfree_mb, cpu_serial: .cpu_serial, date_time: {tz: .date_time.tz}"
# fields="hostname: .hostname, os_family: .os_family, distribution: .distribution, distribution_version: .distribution_version, architecture: .architecture, memtotal_mb: .memtotal_mb, memfree_mb: .memfree_mb, python: .python"

# 全てのJSONファイルを処理
for file in $facts_dir/*.json; do
  # フィールドの情報を抽出
  jq -r "{${fields}}" "$file"
done


# architecture
# uname -m に相当
# x86_64: 64ビットのx86
# armv7l: 32ビットのarm
# aarch64: 64ビットのarm

# デフォルトでストレージやGPUの情報は提供していない
# カスタムfactsを作ることはできるらしい
