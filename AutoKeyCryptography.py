message = list(input())
key = list(int(input()) - 65)
key.extend(message[:len(message) - len(key)])

cypher = list(zip(key, message))

print(len(message), len(key))
print(cypher)

