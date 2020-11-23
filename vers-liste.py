#!/usr/bin/python3
import json
import random
import re
import sys

book_mapping = {
    "1Mo": "1.Mose",
    "2Mo": "2.Mose",
    "3Mo": "3.Mose",
    "4Mo": "4.Mose",
    "5Mo": "5.Mose",
    "Jos": "Josua",
    "Ri": "Richter",
    "Rt": "Rut",
    "1Sam": "1.Samuel",
    "2Sam": "2.Samuel",
    "1Kö": "1.Könige",
    "2Kö": "2.Könige",
    "1Chr": "1.Chronik",
    "2Chr": "2.Chronik",
    "Esr": "Esra",
    "Neh": "Nehemia",
    "Est": "Ester",
    "Hi": "Hiob",
    "Ps": "Psalm",
    "Spr": "Sprüche",
    "Pred": "Prediger",
    "Hl": "Hohelied",
    "Jes": "Jesaja",
    "Jer": "Jeremia",
    "Kla": "Klagelieder",
    "Hes": "Hesekiel",
    "Dan": "Daniel",
    "Hos": "Hosea",
    "Joe": "Joel",
    "Am": "Amos",
    "Ob": "Obadja",
    "Jon": "Jona",
    "Mi": "Micha",
    "Nah": "Nahum",
    "Hab": "Habakuk",
    "Zef": "Zefanja",
    "Hag": "Haggai",
    "Sach": "Sacharja",
    "Mal": "Maleachi",
    "Mt": "Matthäus",
    "Mk": "Markus",
    "Lk": "Lukas",
    "Joh": "Johannes",
    "Apg": "Apostelgeschichte",
    "Röm": "Römer",
    "1Kor": "1.Korinther",
    "2Kor": "2.Korinther",
    "Gal": "Galater",
    "Eph": "Epheser",
    "Phi": "Philipper",
    "Kol": "Kolosser",
    "1Thes": "1.Thessalonicher",
    "2Thes": "2.Thessalonicher",
    "1Tim": "1.Timotheus",
    "2Tim": "2.Timotheus",
    "Tit": "Titus",
    "Phim": "Philemon",
    "Hebr": "Hebräer",
    "Jak": "Jakobus",
    "1Petr": "1.Petrus",
    "2Petr": "2.Petrus",
    "1Jo": "1.Johannes",
    "2Jo": "2.Johannes",
    "3Jo": "3.Johannes",
    "Jud": "Judas",
    "Offb": "Offenbarung",
}

one_chapter_books = ["Jud", "2Jo", "3Jo", "Phim"]

vers_regex = r'(?P<book>([1-5])?[A-Z][a-zäöü]{1,3}) ((?P<chapter>[0-9]{1,3}),)?(?P<vers>[0-9]{1,3})'


class Vers:

    def __init__(self, book, chapter, line):
        if book not in book_mapping.keys():
            print("Unbekanntes Buch")
            sys.exit(1)
        if not chapter:
            if not book in one_chapter_books:
                print("Das Kapitel fehlt")
                sys.exit(1)
        else:
            if book in one_chapter_books:
                print("Dieses Buch hat nur ein Kapitel")
                sys.exit(1)
        self.book = book
        self.chapter = chapter
        self.line = line

    def __str__(self):
        if self.chapter:
            return "{} {},{}".format(
                book_mapping[self.book], self.chapter, self.line)
        else:
            return "{} {}".format(book_mapping[self.book, self.line])
        

def enter_vers():
    input_vers = input("Vers: ")
    result = re.match(vers_regex, input_vers)
    if not result:
        print("Falsches Format")
        return None
    book = result.group("book")
    chapter = result.group("chapter")
    line = result.group("vers")
    return Vers(book, chapter, line)


def save_vers(vers_dict, vers):
    if vers.chapter:
        if vers.chapter not in vers_dict[vers.book].keys():
            vers_dict[vers.book][vers.chapter] = {}
        container = vers_dict[vers.book][vers.chapter]
    else:
        container = vers_dict[vers.book]

    for line in container.keys():
        if line == vers.line:
            print("Dieser Vers ist bereits in der Liste")
            return vers_dict
    container[vers.line] = False
    return vers_dict

def search_vers(vers_dict, vers):
    if vers.chapter:
        if vers.chapter not in vers_dict[vers.book]:
            print("Dieser Vers ist nicht in der Liste")
            return None
        container = vers_dict[vers.book][vers.chapter]
    else:
        container = vers_dict[vers.book]

    if vers.line not in container.keys():
        print("Dieser Vers ist nicht in der Liste")
        return None
    return container

def mark_vers(vers_dict, vers):
    container = search_vers(vers_dict, vers)
    if not container:
        return vers_dict
    container[vers.line] = True
    return vers_dict

def delete_vers(vers_dict, vers):
    container = search_vers(vers_dict, vers)
    if not container:
        return vers_dict
    del container[vers.line]
    return vers_dict

def print_list(vers_dict):
    for book in vers_dict.keys():
        if not vers_dict[book]:
            continue
        print("{}:".format(book_mapping[book]))
        if book not in one_chapter_books:
            for chapter_name, chapter in sorted(
                    vers_dict[book].items(),
                    key=lambda chapter: int(chapter[0])):
                print("  Kapitel {}:".format(chapter_name))
                for line, marked in sorted(
                        chapter.items(),
                        key=lambda line: int(line[0])):
                    if marked:
                        print("    [x] {}".format(line))
                    else:
                        print("    [ ] {}".format(line))
        else:
            for line, marked in sorted(
                    vers_dict[book].items(),
                        key=lambda line: int(line[0])):
                if marked:
                    print("    [x] {}".format(line))
                else:
                    print("    [ ] {}".format(line))

def random_vers(vers_dict):
    unlearned_verses = []
    for book_name, book in vers_dict.items():
        if book_name in one_chapter_books:
            for vers_number, learned in book.items():
                if not learned:
                    unlearned_verses.append(Vers(book_name, None, vers_number))
        else:
            for chapter_number, chapter in book.items():
                for vers_number, learned in chapter.items():
                    if not learned:
                        unlearned_verses.append(
                            Vers(book_name, chapter_number, vers_number))
    vers_index = random.randint(0, len(unlearned_verses))
    print(unlearned_verses[vers_index])

while True:
    print("Wähle eine Operation aus:")
    print("(0) Programm beenden")
    print("(1) Alle Verse ausgeben")
    print("(2) Neuen Vers eingeben")
    print("(3) Stelle als gelernt markieren")
    print("(4) Vers aus System löschen")
    print("(5) Statistik")
    print("(6) Zufälligen Vers lernen")
    
    op = input("Operation: ")

    if op not in ["0","1","2","3","4","5","6",]:
        continue
    if op == "0":
        sys.exit(0)
    else:
        with open("verse.json", "r+") as fp:
            vers_dict = json.load(fp)
        if op == "1":
            print_list(vers_dict)
        elif op == "6":
            random_vers(vers_dict)
        else:
            vers = enter_vers()
            if not vers:
                continue
            if op == "2":
                save_vers(vers_dict, vers)
            elif op == "3":
                mark_vers(vers_dict, vers)
            elif op == "4":
                delete_vers(vers_dict, vers)
            with open("verse.json", "w") as fp:
                json.dump(vers_dict, fp)
    print("")
