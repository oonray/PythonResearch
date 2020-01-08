"""
Reads the Etterspørsel file and prints the data.
"""

def read_csv_data(path):
    """
       Takes a file path and returns lines as list.
    """
    with open(path,"r") as f:
        data = f.read()
    return data.split("\n")

def get_separated_data(line,separator):
    """
        Takes in a line and returns a list
        It will also remove the \" character.
    """
    data = line.split(separator)
    data = [i.replace("\""," ") for i in data]
    data = [i.strip() for i in data]
    return data

def get_index(lines,separator):
    """
     Takes a file as a set of lines and returns the csv index.
    """
    return get_separated_data(lines[0],separator)

def make_list_dict(lines,separator):
    index = get_index(lines,separator)  #List of index
    new_data = list()

    for i in lines[1:]:
        line = get_separated_data(i,separator)
        line_dict = dict()
        for n,x in zip(index,line):
            line_dict[n] = x
        new_data.append(line_dict)
    return new_data


if __name__ == "__main__":
    path = r"./etterspørsel.csv"
    lines = read_csv_data(path)
    lines_assosiativ = make_list_dict(lines,";")
    biggest_year = dict()
    for i in lines_assosiativ:
        biggest_year[i["År"]] = 0
    for i in lines_assosiativ:
        biggest_year[i["År"]] += 1
    print(biggest_year)







