import redis


client = redis.Redis(host="localhost", port=6379)
client.set('test-key', 'test-value')

value = client.get('test-key')
print("hello")
print(value)