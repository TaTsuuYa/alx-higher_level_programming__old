#!/usr/bin/python3
if __name__ == "__main__":
    for i in dir("hidden_4.pyc"):
        if i[:2] != "__":
            print(i)
