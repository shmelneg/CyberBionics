def main():
    hogwarts = {"Gryffindor": 200,
                "Hufflepuff": 112,
                "Ravenclaw": 150,
                "Slytherin": 199
                }
    print("The winner of this year is", whoswinner(hogwarts))

def whoswinner(univercity):
    scores = list(univercity.values())
    for faculty, score in univercity.items():
        if score == max(scores):
            return faculty

if __name__ == '__main__':
    main()