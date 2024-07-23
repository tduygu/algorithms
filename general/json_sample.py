import json

with open('../backup_config.json') as fh:
    conf = json.load(fh)

print(conf)
print(type(conf))
print(conf["read_db"])

conf["new_key"] = 5.56789
with open('../backup_config.json', 'w') as fh:
    # json.dump(conf, fh)
    json.dump(conf, fh, indent=4, separators=(',', ': '))