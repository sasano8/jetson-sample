import os
import json
import asyncio


DIR_FACTS = os.getcwd() + "/facts"


async def watch_and_ingest(interval: int = 60 * 60, dispatcher = lambda x: x):
    "ansibleのfactsファイルを収集し、インデクシングする"

    while True:
        for file in list_all_files(DIR_FACTS):
            spec = await injest(file)
            dispatcher(spec)
        
        await asyncio.sleep(interval)


def list_all_files(src_dir):
    "指定したディレクトリのファイル群をフルパスで返す"
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            yield os.path.join(root, file)



async def injest(file):
    with open(file) as f:
        data = json.load(f)
        alias = ".".join(os.path.splitext(os.path.basename(file))[:-1])
        base = extract_base(alias, data)
        additional = extract_additional(data)
        base.update(additional=additional)
        
        return base


def extract_base(alias, data: dict):
    return {
        "alias": alias,
        "hostname" : data["hostname"],
        "os_family": data["os_family"],
        "distribution": data["distribution"],
        "distribution_version": data["distribution_version"],
        "architecture": data["architecture"],
        "memtotal_mb": data["memtotal_mb"],
        "memfree_mb": data["memfree_mb"],
        "date_time": {k:v for k,v in data["date_time"].items() if k == "tz"},
        "additional": {}
    }


def extract_additional(data: dict):
    return {
        "python": data["python"]
    }
