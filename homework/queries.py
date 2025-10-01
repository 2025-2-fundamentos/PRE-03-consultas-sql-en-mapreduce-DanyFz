"""Taller evaluable"""

import os


def query_1(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "_SUCCESS"), "w", encoding="utf-8") as f:
        f.write("")

    with open(os.path.join(output_dir, "part-00000"), "w", encoding="utf-8") as f:
        f.write("Resultado de la query 1\n")


def query_2(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "_SUCCESS"), "w", encoding="utf-8") as f:
        f.write("")

    with open(os.path.join(output_dir, "part-00000"), "w", encoding="utf-8") as f:
        f.write("Resultado de la query 2\n")


def query_3(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "_SUCCESS"), "w", encoding="utf-8") as f:
        f.write("")

    with open(os.path.join(output_dir, "part-00000"), "w", encoding="utf-8") as f:
        f.write("Resultado de la query 3\n")


def query_4(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "_SUCCESS"), "w", encoding="utf-8") as f:
        f.write("")

    with open(os.path.join(output_dir, "part-00000"), "w", encoding="utf-8") as f:
        f.write("Resultado de la query 4\n")


def query_5(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "_SUCCESS"), "w", encoding="utf-8") as f:
        f.write("")

    with open(os.path.join(output_dir, "part-00000"), "w", encoding="utf-8") as f:
        f.write("Resultado de la query 5\n")

# pylint: disable=broad-exception-raised
# pylint: disable=import-error


#
# ORQUESTADOR:
#
def run():
    """Orquestador"""
    query_1("files/query_1/")
    query_2("files/query_2/")
    query_3("files/query_3/")
    query_4("files/query_4/")
    query_5("files/query_5/")
    
if __name__ == "__main__":

    run()