import random
import json
import os

count = int(os.getenv("FILE_COUNT", 100))

with open('/usr/share/dict/words') as f:
    all_words = f.readlines()

words = [word.strip() for word in all_words]

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        "topic": random.choice(words),
        "amount": "%.2f" % amount
    }

    with open(f"./new/receipt-{identifier}.json", 'w') as f:
        json.dump(content, f)
