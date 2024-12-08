from collections import Counter


def predict_party_victory(senate: str) -> str:
    response = {"R": "Radiant", "D": "Dire"}
    if len(senate) == 1 or len(senate) == 2:
        return response[senate[0]]

    counter = Counter(senate)
    number_dire_senators = counter["D"]
    number_radiant_senators = counter["R"]
    dire_banned = 0
    radiant_banned = 0
    queue = [senator for senator in senate]
    while len(queue) > 0:
        senator = queue.pop(0)
        if senator == "R":
            if radiant_banned > 0:
                number_radiant_senators -= 1
                radiant_banned -= 1
            else:
                if number_dire_senators <= 1:
                    return response[senator]
                dire_banned += 1
                queue.append(senator)
        else:
            if dire_banned > 0:
                number_dire_senators -= 1
                dire_banned -= 1
            else:
                if number_radiant_senators <= 1:
                    return response[senator]
                radiant_banned += 1
                queue.append(senator)
