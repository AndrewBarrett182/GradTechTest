medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def createMedalTable(results):

    scores = {}

    for i in results:
        for j in i["podium"]:
            medal = j.split(".")
            if medal[1] not in scores:
                if int(medal[0]) == 1:
                    scores[medal[1]] = 3
                elif int(medal[0]) == 2:
                    scores[medal[1]] = 2
                elif int(medal[0]) == 3:
                    scores[medal[1]] = 1
            else:
                if int(medal[0]) == 1:
                    scores[medal[1]] = scores[medal[1]] + 3
                elif int(medal[0]) == 2:
                    scores[medal[1]] = scores[medal[1]] + 2
                elif int(medal[0]) == 3:
                    scores[medal[1]] = scores[medal[1]] + 1
    return scores


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
