import os
import glob
import json
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already exists")

# receipts = glob.glob("./new/receipt-[0-9]*.json")

subtotal = 0.0

for path in glob.iglob("./new/receipt-[0-9]*.json"):
    with open(path) as file:
        content = json.load(file)
        subtotal += float(content['amount'])
    destination = path.replace('new', 'processed')
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")

print(f"Receipt subtotal: ${round(subtotal, 2)}")
