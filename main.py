from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  new_list1 = []
  new_list2 = []
  resulting_list = []
#pprint(contacts_list)


def move_the_names():
    for column in contacts_list:
        string = " ".join(column[:3])
        res = string.split()
        if len(res) == 3:
            res.extend(column[3:])
        elif len(res) == 2:
            res.extend(column[2:])
        else:
            res.extend(column[1:])
        new_list1.append(res)
    return new_list1


def format_phone_number():
    pattern = re.compile("(\+7|8) ?\(?(\d{3})\)? ?-?(\d{3})-?(\d{2})-?(\d{2})(\s|,)?\(?(доб.)? ?(\d{4})?\)?")
    substitution = r'+7(\2)\3-\4-\5\6\7\8'
    for column in new_list1:
        string = ','.join(column)
        subs = pattern.sub(substitution, string)
        res = subs.split(',')
        new_list2.append(res)
    return new_list2


def combine_all_duplicate_records():
    for column in new_list2[1:]:
        first_name = column[0]
        last_name = column[1]
        for contact in new_list2:
            new_first_name = contact[0]
            new_last_name = contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if column[2] == '':
                    column[2] = contact[2]
                if column[3] == '':
                    column[3] = contact[3]
                if column[4] == '':
                    column[4] = contact[4]
                if column[5] == '':
                    column[5] = contact[5]
                if column[6] == '':
                    column[6] = contact[6]

    for contact in new_list2:
        if contact not in resulting_list:
            resulting_list.append(contact)
    return resulting_list


if __name__ == '__main__':
    move_the_names()
    format_phone_number()
    combine_all_duplicate_records()

    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(resulting_list)
