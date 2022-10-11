class Gallows():
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if len(self.words) > 0:
            if self.words[-1][-1] == word[0] and word not in self.words:
                self.words.append(word)
                return self.words
            else:
                self.game_over = True
                return "game over"
        else:
            self.words.append(word)
            return self.words

    def restart(self):
        self.game_over = False
        self.words = []
        return "game restarted"
