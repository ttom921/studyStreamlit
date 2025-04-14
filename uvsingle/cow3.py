# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "cowsay",
#     "rich",
# ]
# ///

from cowsay import cow
from rich import print
def main() -> None:
    cow('hello, uv')
    print("Hello rich")


if __name__ == "__main__":
    main()
