import sys
import csv


def main():
      try:
        if len(sys.argv) < 3:
            sys.exit("Too few command line arguments")

        elif len(sys.argv) > 3:
            sys.exit("Too many command line arguments")

        else:
            names = []
            with open(sys.argv[2], "w") as file:
                    writer0 = csv.writer(file)
                    writer0.writerow(["first","last","house"])

            with open(sys.argv[1], 'r') as file:
                let_see = csv.DictReader(file)
                for dict in let_see:
                    names = dict["name"].split(",")
                    del dict["name"]
                    dict["last"] = names[0]
                    dict["first"] = names[1].strip()
                    with open(sys.argv[2], "a") as file:
                        writer1 = csv.DictWriter(file, fieldnames=["first", "last","house"])
                        writer1.writerow(dict)

      except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()