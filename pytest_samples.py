from typing import List

def join(xs: List[int], denom: str) -> None:
    return denom.join(str(i) for i in xs)