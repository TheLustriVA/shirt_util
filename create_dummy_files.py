name_list = []

for idx in range(0,20):
    name_list.append(f"file #{idx} is Kieran's.md")

print(name_list)

for filename in name_list:
    with open(filename, 'w') as f:
        f.write("This is a dummy file.")