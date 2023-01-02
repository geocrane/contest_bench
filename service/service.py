import sys
import settings
from typing import List, Callable


def get_lines(file_path: str) -> List:
    """Возвращает список строк из файла"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().splitlines()


def write_input(file: str, data: List, index: int) -> None:
    """
    Записывает в файл строки из списка, пока
    не достигнет указателя о начале строк с ответами.
    """
    for idx in range(index + 1, len(data)):
        if data[idx] == settings.DATA_OUT_MARKER:
            return
        file.write(f"{data[idx]}\n")


def write_output(file: str, data: List, index: int) -> None:
    """
    Записывает в файл строки из списка, пока
    не достигнет указателя о начале строк с входными данными.
    """
    for idx in range(index + 1, len(data)):
        if data[idx] == settings.DATA_IN_MARKER:
            return
        file.write(f"{data[idx]}\n")


def task_parse() -> None:
    """
    Разделяет общий файл с входными данными и ответами на два отдельных файла.
    Удаляет пустые строки. Расставляет маркеры между группами входных данных и
    ответов для разных тестов.
    """
    with open(settings.INPUT_FILE, "w", encoding="utf-8") as input:
        with open(settings.OUTPUT_FILE, "w") as output:
            data = get_lines("data.txt")
            if (
                settings.DATA_IN_MARKER not in data
                or settings.DATA_OUT_MARKER not in data
            ):
                raise ValueError(
                    "Убедитесь, что в файле data.txt входные данные и ответы "
                    "разделены тем же маркером, как указано в settings. "
                    "По умолчанию: 'in' и 'out'."
                )
            cleaned_data = [line for line in data if len(line.strip())]
            for index, line in enumerate(cleaned_data):
                if line == settings.DATA_IN_MARKER:
                    input.write(f"{settings.SEPARATOR}\n")
                    write_input(input, cleaned_data, index)
                if line == settings.DATA_OUT_MARKER:
                    output.write(f"{settings.SEPARATOR}\n")
                    write_output(output, cleaned_data, index)
            output.write(settings.SEPARATOR)
            input.write(settings.SEPARATOR)


def duplicate() -> Callable:
    """
    Создает копию основной программы из bench.py.
    Заменяет конструкцию 'if __name__ == __main__' на вызываемую функцию.
    Заменяет ввод с клавиатуры input() на чтение из файла readlines().
    Возвращает функцию для вызова копии основной программы.
    """
    with open("bench.py", "r") as bench:
        with open("service/bench_temp.py", "w") as bench_temp:
            lines = bench.readlines()
            if 'if __name__ == "__main__":\n' not in lines:
                raise ValueError("Поместите исполняемый код в блок if__name__=='__main__:'")
            for line in lines:
                if line.startswith("if __name__ =="):
                    bench_temp.write("def call_main(file_path):\n")
                elif "input()" in line:
                    bench_temp.write(
                        line.replace(
                            "input()", "file_path.readline().rstrip()"
                        )
                    )
                else:
                    bench_temp.write(line)
    from service.bench_temp import call_main
    return call_main


def assertion_full(test: int) -> None:
    """
    Производит сравнение ответа программы с ожидаемым ответом.
    Выводит в консоль полный итог сравнения.
    """
    calc = get_lines(settings.RESULT_FILE)
    input = get_lines(settings.INPUT_FILE)
    output = get_lines(settings.OUTPUT_FILE)

    if settings.CLEAN_SPACES:
        calc = [line.strip() for line in calc]

    if calc != output:
        print(f"ТЕСТ {test + 1}: ОШИБКА!")
        print("Входные данные:")
        for line in input:
            print(line)
        print("\nВывод программы:")
        for line in calc:
            print(line)
        print("\nПравильный ответ:")
        for line in output:
            print(line)
        print("-" * 20)
    else:
        print(f"TEST {test + 1}: ОК!")


def assertion_short(test: int) -> None:
    """
    Производит сравнение ответа программы с ожидаемым ответом.
    Выводит в консоль краткий итог сравнения.
    """
    calc = get_lines(settings.RESULT_FILE)
    output = get_lines(settings.OUTPUT_FILE)

    if settings.CLEAN_SPACES:
        calc = [line.strip() for line in calc]

    if calc != output:
        print(
            f"ТЕСТ {test + 1}: ОШИБКА! Получены строки: {calc} "
            f"// Правильно: {output}"
        )
    else:
        print(f"TEST {test + 1}: ОК!")


def launch(func: Callable) -> None:
    """
    Разделяет общие файлы с входными данными и ответами на отдельные группы
    для каждого теста. Запускает копию основной программы, передавая файл с
    входными данными для тестов и ответами для сравнения с результатом.
    """

    all_inputs = get_lines(settings.INPUT_FILE)
    all_outputs = get_lines(settings.OUTPUT_FILE)
    input_sep = [
        index
        for index, slice in enumerate(all_inputs)
        if slice == settings.SEPARATOR
    ]
    output_sep = [
        index
        for index, slice in enumerate(all_outputs)
        if slice == settings.SEPARATOR
    ]
    if len(input_sep) != len(output_sep):
        raise ValueError(
            "Убедитесь, что файл data.txt заполнен верно. Для каждого набора "
            "входных данных должен быть указан ожидаемый ответ."
        )
    zip_inputs = list(zip(input_sep, input_sep[1:]))
    zip_outputs = list(zip(output_sep, output_sep[1:]))

    for test in range(0, len(input_sep) - 1):
        with open(settings.INPUT_FILE, "w") as input:
            for line in range(zip_inputs[test][0] + 1, zip_inputs[test][1]):
                input.write(all_inputs[line] + "\n")
        with open(settings.OUTPUT_FILE, "w") as output:
            for line in range(zip_outputs[test][0] + 1, zip_outputs[test][1]):
                output.write(all_outputs[line].strip() + "\n")
        stdout_original = sys.stdout
        with open(settings.RESULT_FILE, "w") as sys.stdout:
            with open(settings.INPUT_FILE, "r") as input:
                func(input)
        sys.stdout = stdout_original
        if settings.ASSERTIONS_SHORT_FORMAT:
            assertion_short(test)
        else:
            assertion_full(test)


def test() -> None:
    """Запускает функции тестировщика"""
    task_parse()
    launch(duplicate())
