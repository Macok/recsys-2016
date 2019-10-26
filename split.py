import random

header = False
interactions_test_buf = {}
interactions_for_test = set()

for line in open('data_modified/interactions.csv', 'r'):
    if not header:
        header = True
        continue

    elems = line.split()
    user_id = int(elems[0])
    item_id = int(elems[1])

    if random.random() < 1.0 / 5.0:
        interactions_for_test.add((user_id, item_id))

header = False
with open('data_modified/interactions_train.csv', 'w+') as train:
    for line in open('data_modified/interactions.csv', 'r'):
        if not header:
            train.write(line)
            header = True
            continue

        elems = line.split()
        user_id = int(elems[0])
        item_id = int(elems[1])
        if (user_id, item_id) in interactions_for_test:
            if user_id not in interactions_test_buf:
                interactions_test_buf[user_id] = set()
            interactions_test_buf[user_id].add(item_id)
        else:
            train.write(line)

with open('data_modified/interactions_test.csv',
          'w+') as test:
    for user_id, item_set in interactions_test_buf.items():
        test.write(str(user_id) + "," + ' '.join([str(i) for i in item_set]))
        test.write('\n')
