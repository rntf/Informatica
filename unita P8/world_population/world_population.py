def main():
    try:
        infile = open("populations.txt", "r")
        record = extract_record(infile)
        while len(record) > 0:
            print(f"{record['country']:20s} {record['population']:10d}")
            record = extract_record(infile)
        infile.close()
    except FileNotFoundError:
        print("Errore nell'apertura del file")


def extract_record(infile):
    record = {}
    line = infile.readline()
    if line != "":
        fields = line.split(":")
        record["country"] = fields[0]
        record["population"] = int(fields[1])
    return record


main()
