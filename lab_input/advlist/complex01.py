#!/usr/bin/env python3

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)
    
    # print second element of list1
    print(list1[1])

    # create a new list containing a single item
    list2 = ["juniper"]

    # extend the list1 by list2 to combine them together to make a new list
    list1.extend(list2)

    # print the list
    print(list1)

    # create a third list
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # use the append operation to append list1 by list3
    list1.append(list3)

    # display the new complex list
    print(list1)

    # print the list of the IP addresses
    print(list1[4])

    # display the first item in the list, first IP address
    print(list1[4][0])
main()

