import json
s = '{"A": {"X": 1, "Y": 1.0, "Z": "abc"}, "B": [true, false, null, NaN, Infinity]}'

d = json.loads(s)
print(d)
# {'A': {'X': 1, 'Y': 1.0, 'Z': 'abc'}, 'B': [True, False, None, nan, inf]}

print(type(d))