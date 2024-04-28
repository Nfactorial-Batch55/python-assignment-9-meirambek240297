def swap_dict(d: dict) -> dict:
    d_swap = {v: k for k, v in d.items()}
    return d_swap

print(swap_dict({'a': 1, 'b': 1}))