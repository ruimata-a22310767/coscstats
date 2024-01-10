from dataclasses import dataclass, field
from typing import List

@dataclass
class Settings:
    name: str
    age: int
    email: str
    is_student: bool = True
    grades: List[float] = field(default_factory=list)

    def add_grade(self, grade: float):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

# Example usage:
person = ComplexData(name="John Doe", age=25, email="john@example.com")
person.add_grade(85.5)
person.add_grade(92.0)
average_grade = person.calculate_average_grade()

print(f"{person.name} ({person.age} years old) has an average grade of {average_grade:.2f}.")
