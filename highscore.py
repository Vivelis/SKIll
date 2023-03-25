def parse_score():
    i = 0
    names_scores = []
    with open("highscores.txt", "r") as fichier:
        for lines in fichier:
            highscores = lines.strip()
            names_scores.append(highscores.split(" "))
    names_scores.sort(key=lambda x: int(x[1]), reverse=True)
    return names_scores

def add_score(name, score):
    fichier = open("highscores.txt", "a")
    fichier.write(name + " " + str(score) + "\n")
    fichier.close()