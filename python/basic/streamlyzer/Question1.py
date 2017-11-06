class Shipping:
    # Returns integer, the minimum number of packages needed to hold a given number of items
    @staticmethod
    def minimal_number_of_packages(items, available_large_packages, available_small_packages):
        available = (available_large_packages * 5 + available_small_packages)
        if items > available:
            return -1

        big = 0
        for b in range(available_large_packages):
            if items - 5 > 0:
                items = items - 5
                big += 1
            available_large_packages -= 1

        small = 0
        for s in range(available_small_packages):
            if items - 1 >= 0:
                items = items - 1
                small += 1
            available_small_packages -= 1

        if items > 0 or available_large_packages < 0 or available_small_packages < 0:
            return -1

        return big + small


print(Shipping.minimal_number_of_packages(16, 2, 10))
