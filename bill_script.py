from tabula import read_pdf
import sys


REQUIRED_BILLS = {
    "Холодное водоснабжение",
    "Холодное водоснабжение для горячего",
    "Тепловая энергия для ГВ",
    "Водоотведение",
    "Электроэнергия",
    "Отопление",
}


def get_sum_bills(filename: str, column_num:int) -> float:
    if filename[-4:] != ".pdf":
        print(f"Файл {filename} не является pdf")
        return
    df = read_pdf(f"{filename}",pages="all")[2]
    sum_bills = 0
    for _, row in df.iterrows():
        if row.iloc[0] in REQUIRED_BILLS:
            sum_bills += float(row.iloc[column_num].replace(',',".")) if row.iloc[column_num] != '-' else 0
    return round(sum_bills,2)


def main() -> None:
    if len(sys.argv) < 3:
        print("Пожалуйста укажите в аргументе номер колонки расчета и путь до pdf-файла с счетом")
        return
    if not sys.argv[1].isdigit():
        print(f"Номер колонки должен быть числом!!! Введено: {sys.argv[1]}")
        return
    column_num = int(sys.argv[1]) - 1
    for filename in sys.argv[2:]:
       sum_bills = get_sum_bills(filename,column_num)
       print(f"Сумма счетов для {filename}: {sum_bills}")



if __name__ == "__main__":
    main()
