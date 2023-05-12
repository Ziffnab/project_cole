import os
import random
import string
from typing import Dict, Any

class MrData:
    def __init__(self, name: str, age: int, occupation: str, interests: List[str], education: List[str]):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.interests = interests
        self.education = education
    
    def get_random_fact(self) -> str:
        facts = [
            "I am a fan of science fiction movies.",
            "I enjoy reading books on philosophy.",
            "I have a pet cat named Whiskers.",
            "I have traveled to Europe multiple times.",
            "I am fluent in Japanese."
        ]
        return random.choice(facts)
    
    def save_memory(self, key: str, value: Any) -> None:
        if key in self.__dict__:
            data = {k: v for k, v in self.__dict__.items() if k != key}
            with open('memory.json', 'w') as f:
                json.dump(data, f)
        else:
            raise KeyError(f"Key '{key}' not found in memory.")
    
    def load_memory(self, key: str) -> Any:
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            raise KeyError(f"Key '{key}' not found in memory.")
    
    def delete_memory(self, key: str) -> None:
        if key in self.__dict__:
            del self.__dict__[key]
            with open('memory.json', 'w') as f:
                json.dump(self.__dict__, f)
        else:
            raise KeyError(f"Key '{key}' not found in memory.")

def main():
    pass

if __name__ == '__main__':
    mr_data_instance = MrData("John Doe", 25, "Software Engineer", ["Soccer", "Reading"], ["Bachelor of Science in Computer Science"])
    mr_data_instance.save_memory("name", "John Doe")
    mr_data_instance.load_memory("name")
    mr_data_instance.delete_memory("name")

# Additional code to access the local system and set up the
    mr_data_instance.save_memory("age", 25)
    mr_data_instance.load_memory("age")
    mr_data_instance.delete_memory("age")

    mr_data_instance.save_memory("occupation", "Software Engineer")
    mr_data_instance.load_memory("occupation")
    mr_data_instance.delete_memory("occupation")

    mr_data_instance.save_memory("interests", ["Soccer", "Reading"])
    mr_data_instance.load_memory("interests")
    mr_data_instance.delete_memory("interests")

    mr_data_instance.save_memory("education", ["Bachelor of Science in Computer Science"])
    mr_data_instance.load_memory("education")
    mr_data_instance.delete_memory("education")

    mr_data_instance.save_memory("random_fact", mr_data_instance.get_random_fact())
    mr_data_instance.load_memory("random_fact")
    print(mr_data_instance.load_memory("random_fact"))

if __name__ == '__main__':
    main()
