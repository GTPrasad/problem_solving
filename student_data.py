# student record class file.


class Student:
    def __init__(self):
        self.records = []

    def record(self, age, number, name):
        temp = {"age": age, "number": number, "name": name}
        self.records.append(temp)
        return self.records

    def age_sort(self):
        lst_age = [x["age"] for x in self.records]
        lst_age.sort()
        return lst_age

    def number_sort(self):
        lst_number = [x["number"] for x in self.records]
        lst_number.sort()
        return lst_number

    def ages(self):
        if len(self.records) > 1:
            for i in range(len(self.records)):
                for j in range(i + 1, len(self.records)):
                    if self.records[i]["age"] > self.records[j]["age"]:
                        temp = self.records[i]
                        self.records[i] = self.records[j]
                        self.records[j] = temp
            return print(self.records)
        else:
            return print(self.records)

    def numbers(self):
        if len(self.records) > 1:
            for i in range(len(self.records)):
                for j in range(i + 1, len(self.records)):
                    if self.records[i]["number"] > self.records[j]["number"]:
                        temp = self.records[i]
                        self.records[i] = self.records[j]
                        self.records[j] = temp
            return print(self.records)
        else:
            return print(self.records)


stud = Student()
stud.record(17, 200, "Prasad")
stud.record(18, 102, "Prasad1")
stud.record(14, 105, "Prasad2")

stud.ages()
stud.numbers()
