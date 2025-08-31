from file_opp import read_storage, write_storage
from rich import print
from rich.prompt import Prompt
from rich.console import Console

console = Console()


def read(place="main"):
    if place.strip() == "sub":
        v = read_storage("sub")
    else:
        v = read_storage()

    if not len(v):
        print("⚠️[red]empty list can't read[/red]")
        return "er".strip()
    else:
        for i in v:
            print(f"[red]{v.index(i)}[/red].{i}")


def menu():
    print("[green][bold]SELECT OPERATION[/bold][/green]")
    opp = [
        "view task",
        "add task",
        "remove",
        "view history",
        "tick☑️",
        "clear all",
        ".exit",
    ]
    for i in opp:
        print(f"[red]{opp.index(i)}[/red].{i}")
    choise = []
    for i in range(len(opp)):
        choise.append(str(i))
    c = Prompt.ask("[red]choose operation index : [/red]", choices=choise)
    return int(c)


def add():
    s = read_storage()
    print("⚠️after adding tasks enter .exit")
    n = []
    while True:
        i = Prompt.ask("[red]Enter the task : [/red]")
        if i.strip() == ".exit":
            break
        else:
            if i.strip() == "" or i.strip() == " ":
                pass
            else:
                s.append(i)

    write_storage(s)


def remove():
    s = read_storage()

    if not len(s):
        print("[red]⚠️empty[/red]")
    else:
        print("⚠️after deleting tasks enter .exit")
        while True:
            for i in s:
                print(f" [red]{s.index(i)}[/red]. {i} ", end="/")

            print("")

            ix = []
            for i in s:
                ix.append(str(s.index(i)))
            ix.append(".exit".strip())

            inn = Prompt.ask("enter the index of task : ", choices=ix)

            if inn == ".exit":
                break
            else:
                if not len(s):
                    print("[red]⚠️empty[/red]")
                    break
                else:
                    del s[int(inn)]
    write_storage(s)


def history():
    ms = read_storage()
    ss = read_storage("sub")
    if not len(ms) and not len(ss):
        print("[red]⚠️no history found[/red]")
    else:
        st = []
        for i in ss:
            st.append(f"{i} [purple][[green]_/[/green]][/purple]")
        os = st + ms

        for i in os:
            print(f"[red]{os.index(i)}[/red].{i}")


def tick():
    s = read_storage()
    sb = read_storage("sub")
    a = read()
    if a == "er":
        print("⚠️[red]list empty , can't tick[/red]")
    else:
        ix = []
        for i in s:
            ix.append(f"{s.index(i)}")
        ix.append(".exit")
        inn = Prompt.ask("enter the index to tick : ", choices=ix)

        if inn == ".exit":
            print("[green]no task ticked[/green]")
        else:
            t = s[int(inn)]
            del s[int(inn)]

            sb.append(t)

            write_storage(cont=sb, name="sub")
            write_storage(cont=s)


def clear():
    i = Prompt.ask(
        "[red][bold]do you want to delete all the task and progress : [/bold][/red] [green](y/n)[/green]",
        choices=["y", "n", "Y", "N"],
        show_choices=False,
    ).lower()
    if i.lower() == "y":
        write_storage([], "main")
        write_storage([], "sub")
        print("[green]now your list is empty[/green]")
    else:
        print("[green]not cleared[/green]")

def showmain():
    a = read_storage()
    b = read_storage("sub")
    c =b+a

    for i in c:
        if i in b:
            print(f"[red]{c.index(i)}[/red].{i} ☑️")
        else:
            print(f"[red]{c.index(i)}[/red].{i}")
