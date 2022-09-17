import re


def main():
    # phrase = input("Enter your name, phone number, email and feedback: ")
    phrase = "Andrii Melnyk shmelneg@gmail.com +38-068-920-23-96 I liked the course a lot"
    print("==============================")
    student = parse(phrase)
    print("Here is the profile:")
    for key in student:
        print(f"{key}: {student[key]}")


def parse(text):
    output = {}
    output["name"] = re.search(r"[A-Z]\w+\s[A-Z]\w+", text).group(0)
    output["email"] = re.search(r"\S+@\S+", text).group(0)
    output["phone"] = re.search(r"\+?\d+-?\d+-?\d+-?\d+-?\d+", text).group(0)
    feedback = text.replace(output["name"], "").replace(output["email"], "").replace(output["phone"], "").strip()
    output["review"] = feedback
    return output


if __name__ == "__main__":
    main()
