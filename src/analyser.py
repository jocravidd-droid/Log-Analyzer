import json
from pathlib import Path


# Ouvre le fichier des .log et le distribue
def open_file(journal):
    try:
        p = Path.cwd() / journal
        if p.suffix != ".log":
            raise ValueError("un fichier .log")
        with open(journal) as f:
            contenu = f.read()
        return contenu
    except (ValueError, FileNotFoundError) as e:
        print(f"[ERROR] {e}")


def chercheur_ip():
    try:
        ligne = "-" * 3
        with open("result/information_info.json") as f:
            contenu_info = json.load(f)
        copy = contenu_info.copy()
        ip_info = f"\n{ligne}IP INFO{ligne}"
        for key in copy:
            old_c = str(key).split(" ")
            new_c = old_c[1]
            ip_info += f"\nIP: {new_c}"
        with open("result/information_warning.json") as f:
            contenu_warning = json.load(f)
        copy = contenu_warning.copy()
        ip_warning = f"\n{ligne}IP WARNING{ligne}"
        for key_2 in copy:
            old_c = str(key_2).split(" ")
            new_c = old_c[1]
            ip_warning += f"\nIP: {new_c}"
        with open("result/information_error.json") as f:
            contenu_error = json.load(f)
        copy = contenu_error.copy()
        ip_error = f"\n{ligne}IP ERROR{ligne}"
        for key_3 in copy:
            old_c = str(key_3).split(" ")
            new_c = old_c[1]
            ip_error += f"\nIP: {new_c}"
        ip = ip_error + "\n" + ip_warning + "\n" + ip_info
        return ip
    except FileNotFoundError:
        print("Fichier inexistant ou Introuvable")


# retire des
def filtre(choice, ip=None):
    try:
        if ip is None:
            if choice.lower() == "error":
                with open("result/information_error.json") as f:
                    contenu = json.load(f)
            elif choice.lower() == "warning":
                with open("result/information_warning.json") as f:
                    contenu = json.load(f)
            elif choice.lower() == "info":
                with open("result/information_info.json") as f:
                    contenu = json.load(f)
            else:
                return "Choix Inconnu"
            return contenu
        else:
            if choice.lower() == "error":
                with open("result/information_error.json") as f:
                    contenu = json.load(f)
                    copy = contenu.copy()
                    message = ""
                    for c, value in zip(copy.keys(), copy.values()):
                        old_c = str(c).split(" ")
                        new_c = old_c[1]
                        if new_c == ip:
                            message += f"\nIP: {new_c}\nContenu: {value}"
                    return message
            elif choice.lower() == "warning":
                with open("result/information_warning.json") as f:
                    contenu = json.load(f)
                    copy = contenu.copy()
                    message = ""
                    for c, value in zip(copy.keys(), copy.values()):
                        old_c = str(c).split(" ")
                        new_c = old_c[1]
                        if new_c == ip:
                            message += f"\nIP: {new_c}\nContenu: {value}"
                    return message
            elif choice.lower() == "info":
                with open("result/information_info.json") as f:
                    contenu = json.load(f)
                    copy = contenu.copy()
                    message = ""
                    for c, value in zip(copy.keys(), copy.values()):
                        old_c = str(c).split(" ")
                        new_c = old_c[1]
                        if new_c == ip:
                            message += f"\nIP: {new_c}\nContenu: {value}"
                    return message
            else:
                return "Choix Inconnue"
    except (ValueError, FileNotFoundError, AttributeError) as v:
        print(f"[ERROR] : {v}")


# Crée un rapport résument le nombre de warning, error, info et les enregistre séparement sous forme de .json
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


# Ouvre le fichier .log et Crée le dictionnaire et fournis aussi le nombre de warning, error, info
def main(doc):
    try:
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
    except (FileNotFoundError, ValueError) as e:
        print(f"[ERROR] : {e}")


if __name__ == "__main__":
    e, w, i, ed, wd, idi = main("journal.log")
    rapport(e, w, i, ed, wd, idi)
    print(chercheur_ip())
    f = filtre("warning", "45.132.89.10")
    masquer = True
    if masquer:
        with open(".registre.txt", "a") as r:
            ecrit = "\n" + str(f)
            recherche = r.write(ecrit)
    else:
        with open("registre.txt", "a") as r:
            ecrit = "\n" + str(f)
            recherche = r.write(ecrit)
