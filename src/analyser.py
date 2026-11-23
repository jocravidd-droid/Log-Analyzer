import json
from pathlib import Path


def open_file(journal):
    with open(f"../{journal}") as f:
        contenu = f.read()
    return contenu


def filtre(choice):
    if choice.lower() == "error":
        with open("result/information_error.json") as f:
            contenu = json.load(f)
    elif choice.lower() == "warning":
        with open("result/information_warning.json") as f:
            contenu = json.load(f)
    elif choice.lower() == "info":
        with open("result/information_info.json") as f:
            contenu = json.load(f)
    return contenu


def rapport(
    numbre_error, number_warning, number_info, dict_error, dict_warning, dict_info
):
    resume = (
        "Resumer :\n"
        + "Nombre d'info: "
        + str(number_info)
        + "\n"
        + "Nombre de warning: "
        + str(number_warning)
        + "\n"
        + "Nombre d'erreur: "
        + str(numbre_error)
    )
    p = Path("result/")
    p.mkdir(parents=True, exist_ok=True)
    with open("result/resumer.txt", "w") as res:
        contenu = res.write(resume)
    with open("result/information_error.json", "w") as file_e:
        json.dump(dict_error, file_e, indent=4, ensure_ascii=False)
    with open("result/information_warning.json", "w") as file_w:
        json.dump(dict_warning, file_w, indent=4, ensure_ascii=False)
    with open("result/information_info.json", "w") as file_i:
        json.dump(dict_info, file_i, indent=4, ensure_ascii=False)


def main(doc):
    fichier = open_file(doc)
    new_file = fichier.split("\n")
    error = 0
    warning = 0
    info = 0
    error_dict = {}
    warning_dict = {}
    info_dict = {}
    for n in new_file:
        if n.find("ERROR") == -1:
            if n.find("WARNING") == -1:
                if n.find("INFO") == -1:
                    continue
                else:
                    i = n.rsplit("INFO")
                    id_i = i[0].split(" ")
                    info_dict[f"INFO {id_i[2]} : {info}"] = i[1]
                    info += 1
            else:
                w = n.rsplit("WARNING")
                id_w = w[0].split(" ")
                warning_dict[f"WARNING {id_w[2]} : {warning}"] = w[1]
                warning += 1
        else:
            e = n.rsplit("ERROR")
            id_e = e[0].split(" ")
            error_dict[f"ERROR {id_e[2]} : {error}"] = e[1]
            error += 1
    return error, warning, info, error_dict, warning_dict, info_dict


if __name__ == "__main__":
    e, w, i, ed, wd, idi = main("journal.log")
    rapport(e, w, i, ed, wd, idi)
    f = filtre("error")
    print(f)
