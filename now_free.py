

def now_free(price_dict, free_list):
    for prod in free_list:
        price_dict[prod] = 0.0
    return price_dict
