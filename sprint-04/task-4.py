class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    tests_taken = "No tests taken"

    def __init__(self):
        self.dict = {}

    def take_test(self, paper, answer):
        count = 0
        for i in range(len(answer)):
            if paper.markscheme[i] == answer[i]:
                count += 1

        pass_mark = int(paper.pass_mark.replace("%", ""))
        stud_mark = count / len(paper.markscheme) * 100
        if stud_mark >= pass_mark:
            self.dict[paper.subject] = f"Passed! ({stud_mark:.0f}%)"
        else:
            self.dict[paper.subject] = f"Failed! ({stud_mark:.0f}%)"
        self.tests_taken = self.dict
        return self.tests_taken
