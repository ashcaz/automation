import re


def get_emails(file_path="../assets/potential-contacts.txt"):
    # # open potential-contacts.txt
    # with open(file_path, "r") as emails:
    #     content = emails.read()

    # regex = "/\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})/gm"

    # valid_emails = sorted(re.findall(regex, content))
    # # sort
    # # write to file emails.txt
    # return valid_emails
    pass


def get_phone_numbers(file_path="./assets/potential-contacts.txt"):

    with open(file_path, "r") as numbers:
        content = numbers.read()

    valid_phone_numbers = re.findall(
        r"/\(?([0-9]{3})\)?[-.]?([0-9]{3})[-.]?([0-9]{4})/g", content
    )

    # open potential-contacts.txt
    # find all emails using regex
    # sort
    # write to file emails.txt
    return valid_phone_numbers


print(get_phone_numbers())