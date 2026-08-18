

def products(items_purchased):
    if not items_purchased:
        return 0
    return round(sum(items_purchased) + len(items_purchased))
