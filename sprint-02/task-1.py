def double_string(data):
    count = 0
    for i in data:
        if any(i+j in data for j in data):
            count += 1
    return count
