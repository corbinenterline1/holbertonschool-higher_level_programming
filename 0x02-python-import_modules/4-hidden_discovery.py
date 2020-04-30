#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
a = 0
new_list = dir(hidden_4)
l = len(new_list)
while a < l:
    if "__" in new_list[a]:
        a += 1
    else:
        print("{}".format(new_list[a]))
        a += 1
