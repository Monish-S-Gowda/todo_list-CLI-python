from file_opp_fortest import read_storage, write_storage


def inputalist():
    o = []
    while True:
        i = input("enter task to add : ").strip()
        if i == ".exit":
            break
        else:
            if i.strip() == "" or i.strip() == " ":
                pass
            else:
                o.append(i)

    return o


f = inputalist()

write_storage(f)

print(read_storage())

for i in read_storage():
    print(i)
