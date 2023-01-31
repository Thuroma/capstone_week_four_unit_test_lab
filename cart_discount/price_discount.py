def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ 
    Customers that buy three or more products receive the lowest priced item for free.
    This function checks to see if there are three prices in the list.
    If there are, it sorts the list in ascending order.
        Then it returns the lowest value.
    If there are less than three items in the list, return None.
    """
    # TODO Add validation to make sure list contains ints
    # TODO Add validation to make sure list does not contain strings/float

    if len(item_prices) >= 3:
        item_prices.sort()
        return item_prices[0]
    else:
        return None
    




if __name__ == '__main__':
    main()