import re


def main():
    with open('data.txt', 'r') as file1:
        data = file1.read()
        profile = parse(data)
        with open('profile.txt', "w") as file2:
            for key in profile:
                file2.writelines(f"{key}: {profile[key]}\n")


def parse(text):
    output = {}
    output["birthday"] = re.search(r"\d{2}[.-]\d{2}[.-]\d{2,4}", text).group(0)
    output["email"] = re.search(r"\S+@\S+", text).group(0)
    output["phone"] = re.search(r"\+?\d?-?\d{3}-?\d{3}-?\d{2}-?\d{2}", text).group(0)
    return output


if __name__ == "__main__":
    main()
