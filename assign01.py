"""
Assign 01 - MBAMI LUKA

Directions:
    * Complete the linearSearch and binarySearch functions that have been
      started below. Refer to the README.md file for additional info.

    * NOTE: Remember to add a docstring for each function, and that a reasonable
      coding style is followed (e.g. blank lines between functions).
      Your program will not pass the tests if this is not done!
"""
import time
# =====================================================================


def linearSearch(list_of_items, item_sought):
    """Linear Search"""
    num_comparisons = 0
    item_found = False
    first = list_of_items[0]
    last = list_of_items[len(list_of_items) - 1]
    start_time = time.time()

    for item in list_of_items:
        if item == item_sought:
            item_found = True
            elapsed_time = time.time() - start_time
            return (item_found, num_comparisons, elapsed_time)
        num_comparisons += 1

    elapsed_time = time.time() - start_time
    return (item_found, num_comparisons, elapsed_time)
# =====================================================================


def binarySearch(list_of_items, item_sought):
    """Binary Search"""
    num_comparisons = 0
    item_found = False
    first = 0
    last = len(list_of_items) - 1
    start_time = time.time()

    while first <= last:
      mid = (first + last) // 2

      if list_of_items[mid] == item_sought:
        item_found = True
        num_comparisons += 1
        elapsed_time = time.time() - start_time
        return (item_found, num_comparisons, elapsed_time)
      elif list_of_items[mid] < item_sought:
        first = mid + 1
      else:
        last = mid - 1
      num_comparisons += 1

    elapsed_time = time.time() - start_time
    return (item_found, num_comparisons, elapsed_time)
# =====================================================================


def assign01_main():
    """ A 'main' function to be run when our program is run standalone """
    # a sorted list of ~20 items
    list1 = [2, 3, 6, 10, 11, 17, 20, 23, 24, 29, 31, 34, 38, 39, 42, 47, 53]
    item_to_find = 34

    ls_res1 = linearSearch(list1, item_to_find)
    bs_res1 = binarySearch(list1, item_to_find)

    print(f"\nlist1 (size = {len(list1)}) results")
    if ls_res1[0]:
        print("  linear search found the item and required:")
    else:
        print("  linear search did not find the item and required:")
    print("   ", ls_res1[1], "comparisons")
    print(f"    {ls_res1[2]:.4f} seconds")

    if bs_res1[0]:
        print("  binary search found the item and required:")
    else:
        print("  binary search did not find the item and required:")
    print("   ", bs_res1[1], "comparisons")
    print(f"    {bs_res1[2]:.4f} seconds")

    # a sorted list of odds from 1 to 9999
    list2 = list(range(1, 10000, 2))
    item_to_find = -1

    ls_res2 = linearSearch(list2, item_to_find)
    bs_res2 = binarySearch(list2, item_to_find)

    print(f"\nlist2 (size = {len(list2)}) results")
    if ls_res2[0]:
        print("  linear search found the item and required:")
    else:
        print("  linear search did not find the item and required:")
    print("   ", ls_res2[1], "comparisons")
    print(f"    {ls_res2[2]:.4f} seconds")

    if bs_res2[0]:
        print("  binary search found the item and required:")
    else:
        print("  binary search did not find the item and required:")
    print("   ", bs_res2[1], "comparisons")
    print(f"    {bs_res2[2]:.4f} seconds")


# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    assign01_main()
