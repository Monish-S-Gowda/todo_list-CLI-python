from rich.console import Console
from rich.align import Align
from rich.prompt import Confirm
console = Console()
from rich import print
import time
from to_do_opp import read, menu, add, remove, history, tick, clear


def exit(func):
    n = ["read", "add", "remove", "history", "tick", "clear"]
    input(f"press enter key to exit {n[func]} window")


def main():

    console.print(
        Align.center(
            "[bold][underline][blue]TO[/underline] [underline]DO[/underline] [underline]LIST:[/blue][/underline][/bold]"
        )
    )
    time.sleep(1)
    while True:
        a = menu()
        time.sleep(1)
        console.clear()
        if a == 0:
            read()
            exit(a)
        elif a == 1:
            add()
            exit(a)
        elif a == 2:
            remove()
            exit(a)
        elif a == 3:
            history()
            exit(a)
        elif a == 4:
            while True:
                tick()
                console.clear()
                history()
                i = Confirm.ask("want to exit : ")
                if i:
                    console.clear()
                    break
                else:
                    pass
            exit(a)
        elif a == 5:
            clear()
            exit(a)
        elif a == 6:
            
            print("[green][bold]exiting program ...[/bold][/green]")
            time.sleep(1)
            break

    console.clear()


if __name__ == "__main__":
    main()
