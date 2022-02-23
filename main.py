def decorators_(path):
    def decorators(old_func):
        import logging
        import datetime
        logging.basicConfig(level=logging.DEBUG, filename=f'{path}\mylogs.txt', encoding='utf8')

        def new_func(*args, **kwargs):
            result = old_func(*args, **kwargs)
            logging.info(f"Дата и время вызова функции: {datetime.datetime.now()}"
                         f" Имя функции: {old_func.__name__}"
                         f" Аргументы функции: {args, kwargs}"
                         f" Возвращаемое значение: {result}")
            return result
        return new_func
    return decorators


if __name__ == '__main__':

    @decorators_('new_folders')
    def number_people(documents):
        list_number = []
        number = input('Введите номер документа')
        for document in documents:
            list_number.append(document["number"])
            if document["number"] == number:
                print(document["name"])
        if number not in list_number:
            print('Данный документ не найден')
from example import documents
number_people(documents)
