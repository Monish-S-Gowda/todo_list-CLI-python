def read_storage(name="main"):
    if name.strip() == "sub":
        storage = "donestore.txt"
    else:
        storage = "mainstore.txt"

    with open(storage, "r") as file:
        f = file.readlines()
    g = []
    for i in range(len(f) - 1):
        ti = f[i][:-1]
        g.append(ti)
    g.append(f[-1])
    return g


def write_storage(cont: list, name="main"):
    if name.strip() == "sub":
        storage = "donestore.txt"
    else:
        storage = "mainstore.txt"
    if len(cont) == 0:
        with open(storage, "w") as file:
            file.writelines("empty")
    else:
        tc = []
        for i in range(len(cont) - 1):
            tc.append(cont[i] + "\n")

        tc.append(cont[-1])

        with open(storage, "w") as file:
            file.writelines(tc)
