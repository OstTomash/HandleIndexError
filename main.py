def get_item_by_index(items, index):
    """
    Function to get item by index with handling exception
    :param items: string
    :param index: string
    :return: string
    """
    items_list = items.split(' ')

    try:
        index = int(index)
    except ValueError:
        print("Invalid index, will be taken default index (0)")
        index = 0

    try:
        return items_list[index]
    except IndexError:
        print("Invalid index. The last possible index will be taken")
        index = len(items_list) - 1

    return items_list[index]


custom_input = input("Enter items separated by a space: ")
custom_index = input("Enter the index of the item you would like to see: ")
print(get_item_by_index(custom_input, custom_index))
