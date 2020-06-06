import ujson

from jsondiff import diff

# UPDATE
a = {"alpha": 1}
b = {"beta": 2}
output = diff(a, b, syntax='symmetric')
print(ujson.dumps(output))
# > [{"alpha":1},{"beta":2}]

# INSERT
a = {"alpha": 1}
b = {"alpha": 1, "beta": 2}
output = diff(a, b, syntax='symmetric')
print(ujson.dumps(output))
# > {"$insert":{"beta":2}}

# DELETE
a = {"alpha": 1, "beta": 2}
b = {"alpha": 1}
output = diff(a, b, syntax='symmetric')
print(ujson.dumps(output))
# > {"$delete":{"beta":2}}
