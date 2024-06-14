import time
from uuid import UUID
import allure
import pytest_check as check
import re
import difflib
from jsonschema import validate


@check.check_func
def exsistens(param, object, description='!'):
    with allure.step(f"{description}.assert. ОР: "
                     f"Параметр {str(param)[:50]} существует в структуре {str(list(object.keys()))[:50]}"):
        try:
            assert param in object.keys(), f'Не найден параметр в структуре'
        except AssertionError as e:
            allure.attach(param, name="Параметр", attachment_type=allure.attachment_type.TEXT)
            allure.attach(str(list(object.keys())), "Структура", allure.attachment_type.TEXT)
            raise e


@check.check_func
def notExsistens(param, object, description='!'):
    with allure.step(f"{description}.assert. ОР: "
                     f"Параметр {str(param)[:50]} НЕ существует в структуре {str(list(object.keys()))[:50]}"):
        try:
            assert param not in object.keys(), f'Найден параметр в структуре'
        except AssertionError as e:
            allure.attach(param, name="Параметр", attachment_type=allure.attachment_type.TEXT)
            allure.attach(str(list(object.keys())), "Структура", allure.attachment_type.TEXT)
            raise e


@check.check_func
def exsistens_in_list(param, rows, field, description='!'):
    list = [row[f"{field}"] for row in rows]
    with allure.step(f"{description}.assert. ОР: "
                     f"{str(param)[:50]} существует в списке {str(list)[:50]}"):
        try:
            assert param in list, f'Не найдено значение в списке'
        except AssertionError as e:
            allure.attach(param, name="Параметр", attachment_type=allure.attachment_type.TEXT)
            allure.attach(str(list), "Список", allure.attachment_type.TEXT)
            raise e


@check.check_func
def notExsistens_in_list(param, rows, field, description='!'):
    list = [row[f"{field}"] for row in rows]
    with allure.step(f"{description}.assert. ОР: "
                     f"{str(param)[:50]} не существует в списке {str(list)[:50]}"):
        try:
            assert param not in list, f'Найдено значение в списке'
        except AssertionError as e:
            allure.attach(param, name="Параметр", attachment_type=allure.attachment_type.TEXT)
            allure.attach(str(list), "Список", allure.attachment_type.TEXT)
            raise e


@check.check_func
def equals(param1, param2, description='!'):
    with allure.step(f"{description}.assert. ОР: {str(param1)[:50]} == {str(param2)[:50]}"):
        try:
            assert str(param1) == str(param2), f'Некорректное значение параметра. Ожидалось равенство параметров'
        except AssertionError as e:
            allure.attach(str(param1), "Параметр 1", allure.attachment_type.TEXT)
            allure.attach(str(param2), "Параметр 2", allure.attachment_type.TEXT)
            param1 = str(param1).splitlines()
            param2 = str(param2).splitlines()
            d = difflib.Differ()
            diff = d.compare(param1, param2)
            allure.attach(str('\n'.join(diff)), "Различия", allure.attachment_type.TEXT)
            raise e


@check.check_func
def notEquals(param1, param2, description='!'):
    with allure.step(f"{description}.assert. ОР: {str(param1)[:50]} != {str(param2)[:50]}"):
        try:
            assert str(param1) != str(param2), f'Некорректное значение параметра. Ожидалось неравенство параметров'
        except AssertionError as e:
            allure.attach(str(param1), "Параметр 1", allure.attachment_type.TEXT)
            allure.attach(str(param2), "Параметр 2", allure.attachment_type.TEXT)
            param1 = str(param1).splitlines()
            param2 = str(param2).splitlines()
            d = difflib.Differ()
            diff = d.compare(param1, param2)
            allure.attach(str('\n'.join(diff)), "Различия", allure.attachment_type.TEXT)
            raise e


@check.check_func
def regexp(param, reg, description='!'):
    with allure.step(f"{description}.assert. ОР: {str(param)[:50]} соответствует регулярному выражению {str(reg)}"):
        try:
            assert re.match(reg, str(param)), f'Некорректное значение параметра. ' \
                                              f'Ожидалось соответствие регулярному выражению'
        except AssertionError as e:
            allure.attach(str(param), "Параметр", allure.attachment_type.TEXT)
            allure.attach(str(reg), "Регулярное выражение", allure.attachment_type.TEXT)
            raise e


@check.check_func
def contains(param1, param2, description='!'):
    with allure.step(f"{description}.assert. ОР: {str(param1)[:50]} содержится в {str(param2)[:50]}"):
        try:
            assert param1 in param2, f'Некорректное значение параметра. ' \
                                     f'{str(param1)[:50]} не содержится в {str(param2)[:50]}'
        except AssertionError as e:
            allure.attach(str(param1), "Параметр 1", allure.attachment_type.TEXT)
            allure.attach(str(param2), "Параметр 2", allure.attachment_type.TEXT)
            param1 = str(param1).splitlines()
            param2 = str(param2).splitlines()
            d = difflib.Differ()
            diff = d.compare(param1, param2)
            allure.attach(str('\n'.join(diff)), "Различия", allure.attachment_type.TEXT)
            raise e


@check.check_func
def notContains(param1, param2, description='!'):
    with allure.step(f"{description}.assert. ОР: {str(param1)[:50]} НЕ содержится в {str(param2)[:50]}"):
        try:
            assert param1 not in param2, f'Некорректное значение параметра. ' \
                                         f'{str(param1)[:50]} содержится в {str(param2)[:50]}'
        except AssertionError:
            allure.attach(str(param1), "Параметр 1", allure.attachment_type.TEXT)
            allure.attach(str(param2), "Параметр 2", allure.attachment_type.TEXT)
            param1 = str(param1).splitlines()
            param2 = str(param2).splitlines()
            d = difflib.Differ()
            diff = d.compare(param1, param2)
            allure.attach(str('\n'.join(diff)), "Различия", allure.attachment_type.TEXT)


def httpStatusEquals(status, exp_status, description='!'):
    with allure.step(f"{description}.assert. ОР: http статус {str(status)} == {str(exp_status)}"):
        assert status == exp_status, f'Некорректный статус код, ожидалось {exp_status} получено {status}'


def httpStatusContains(status, exp_statusList, description='!'):
    with allure.step(f"{description}.assert. ОР: http статус {str(status)} один из списка {str(exp_statusList)}"):
        assert status in exp_statusList, f'Некорректный статус код, ожидался один из перечня {exp_statusList} получено {status}'


@check.check_func
def notEmpty(param, description='!'):
    with allure.step(f"{description}.assert. ОР: Параметр {str(param)[:50]} имеет НЕ пустое значение"):
        try:
            assert param is not None, f'Некорректное значение параметра. Ожидалось НЕ пустое значение.'
            assert str(param) != "", f'Некорректное значение параметра. Ожидалось НЕ пустое значение.'
            assert len(str(param)) != 0, f'Некорректное значение параметра, Ожидалось НЕ пустое значение.'
        except AssertionError as e:
            allure.attach(str(param), "Параметр", allure.attachment_type.TEXT)
            raise e


@check.check_func
def Empty(param, description='!'):
    with allure.step(f"{description}.assert. ОР: Параметр имеет пустое значение"):
        try:
            assert param is None or str(param) != "", f'Некорректное значение параметра. Ожидалось пустое значение.'
        except AssertionError as e:
            allure.attach(str(param), "Параметр", allure.attachment_type.TEXT)
            raise e


@check.check_func
def more(param1, param2, description='!'):
    with allure.step(f"{description}.assert. ОР: {str(param1)[:50]} > {str(param2)[:50]} "):
        try:
            assert param1 > param2, \
                f'Некорректное значение параметра. Ожидалось {str(param1)[:50]} больше {str(param2)[:50]}'
        except AssertionError as e:
            allure.attach(str(param1), "Параметр 1", allure.attachment_type.TEXT)
            allure.attach(str(param2), "Параметр 2", allure.attachment_type.TEXT)
            raise e


@check.check_func
def less(param1, param2, description='!'):
    with allure.step(f"{description}.assert. ОР: {str(param1)[:50]} < {str(param2)[:50]}"):
        try:
            assert param1 < param2, f'Некорректное значение параметра. Ожидалось {str(param1)[:50]} меньше {str(param2)[:50]}'
        except AssertionError as e:
            allure.attach(str(param1), "Параметр 1", allure.attachment_type.TEXT)
            allure.attach(str(param2), "Параметр 2", allure.attachment_type.TEXT)
            raise e


@check.check_func
def validId(row, description='!'):
    with allure.step(f"{description}.assert. ОР: Корректный ИД"):
        exsistens("id", row)
        notEmpty(row["id"])
        more(row["id"], 0)


@check.check_func
def validUUID(uuid_, description='!'):
    with allure.step(f"{description}.assert. ОР: Корректный UUID"):
        try:
            uuid_obj = UUID(uuid_, version=4)
        except ValueError:
            assert uuid_ == 1, "Не пройдена проверка на корректность UUID"


@check.check_func
def checkAuth(responce, description='!'):
    with allure.step(f"{description}.Проверка Авторизации. Стандарт"):
        httpStatusEquals(responce.status_code, 200)
        exsistens("access_token", responce.json(), "check access_token")
        exsistens("refresh_token", responce.json(), "check refresh_token")
        notEmpty(responce.json()["access_token"], "check access_token")
        notEmpty(responce.json()["refresh_token"], "check refresh_token")


@check.check_func
def checkDateCurrent(date, description='!'):
    with allure.step(f"{description}.assert. ОР: Дата {str(date)} = текущая. Время не учитывается "):
        date = date.split("T")
        equals(date[0], time.strftime("%Y-%m-%d", time.gmtime()))


@check.check_func
def equals_delta(param1, param2, delta, description='!'):
    with allure.step(f"{description}.assert. ОР: {str(param1)[:50]} отличается от {str(param2)[:50]} не больше,"
                     f" чем {str(delta)[:50]} с обеих сторон"):
        try:
            assert abs(
                param1 - param2) <= delta, f'Некорректное значение параметра. Ожидалось {str(param1)[:50]} отличается от' \
                                           f' {str(param2)[:50]} не больше, чем {str(delta)[:50]} с обеих сторон'
        except AssertionError as e:
            allure.attach(str(param1), "Параметр 1", allure.attachment_type.TEXT)
            allure.attach(str(param2), "Параметр 2", allure.attachment_type.TEXT)
            allure.attach(str(delta), "Дельта ожидаемая", allure.attachment_type.TEXT)
            allure.attach(str(abs(param1 - param2)), "Дельта полученная", allure.attachment_type.TEXT)
            raise e


@check.check_func
def equalsListObject(List1, List2, pop_key=0, description='!'):
    with allure.step(f"{description}.assert. ОР: Списки равные: {str(List1)} ==== {str(List2)}"):
        if ((List1 == None or len(List1) == 0) and (List2 == None or len(List2) == 0)):
            return
        if List1 == None or List2 == None or len(List1) == 0 or len(List2) == 0:
            equals(List1, List2)

        if pop_key == 1:
            keys1 = set().union(*(d.keys() for d in List1))
            keys2 = set().union(*(d.keys() for d in List2))

            common_keys = keys1.intersection(keys2)
            List1 = [{k: v for k, v in d.items() if k in common_keys} for d in List1]
            List2 = [{k: v for k, v in d.items() if k in common_keys} for d in List2]

        List1 = sorted(List1, key=lambda x: tuple(x.keys()))
        List2 = sorted(List2, key=lambda x: tuple(x.keys()))

        List1 = sorted(List1, key=lambda x: x['name'])
        List2 = sorted(List2, key=lambda x: x['name'])

        equals(List1, List2, 'Сравнение списков объектов')


@check.check_func
def equalsObject(Obj1, Obj2, description='!'):
    with allure.step(f"{description}.assert. ОР: Объекты равные: {str(Obj1)} ==== {str(Obj2)}"):
        sortObj1 = dict(sorted(Obj1.items()))
        sortObj2 = dict(sorted(Obj2.items()))
        equals(sortObj1, sortObj2, 'Сравнение объектов')


@check.check_func
def checkParamBetween(param, start_param, end_param, description='!'):
    with allure.step(
            f"{description}.assert. ОР: {str(start_param)[:50]} <= {str(param)[:50]} <= {str(end_param)[:50]}"):
        try:
            assert start_param <= param <= end_param, \
                f'Параметр {str(param)[:50]} не входит в диапазон {str(start_param)[:50]} - {str(end_param)[:50]}'
        except AssertionError as e:
            allure.attach(str(start_param), "Начало диапазона", allure.attachment_type.TEXT)
            allure.attach(str(end_param), "Конец диапазона", allure.attachment_type.TEXT)
            allure.attach(str(param), "Параметр", allure.attachment_type.TEXT)
            raise e


@check.check_func
def check_integer(param, description='!'):
    with allure.step(f"{description}.assert. ОР: параметр {str(param)[:50]} целое число"):
        try:
            tmp = int(param)
        except:
            assert 1 == 2, f'Параметр {str(param)} не целое число'


@check.check_func
def validate_schema(schema, data, description='!'):
    with allure.step(f"{description}.Валидация ответа по схеме"):
        try:
            validate(instance=data, schema=schema)
        except Exception as e:
            assert 1 == 2, f'Ошибка валидации ответа по схеме:' + str(e)
