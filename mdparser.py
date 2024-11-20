import markdown
import os
import webbrowser
from markdown.extensions.toc import TocExtension
from markdown.extensions.codehilite import CodeHiliteExtension

def markdown_to_html(input_file):
    # Проверка, существует ли входной файл
    if not os.path.exists(input_file):
        print(f"Файл {input_file} не найден!")
        return
    
    # Чтение содержимого markdown файла
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Преобразуем markdown в HTML с поддержкой оглавления, таблиц и подсветки кода
    html_content = markdown.markdown(markdown_content, extensions=[TocExtension(),'toc','tables',CodeHiliteExtension(linenums=False, guess_lang=True)])

    # Добавляем строку для подключения CSS стилей
    css_link = '<link rel="stylesheet" href="style.css">\n'
    full_html_content = css_link + html_content

    # Получаем имя файла без расширения и добавляем .html
    output_file = os.path.splitext(input_file)[0] + '.html'

    # Записываем результат в HTML файл
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html_content)
        print(f"HTML файл успешно создан: {output_file}")

        # Открываем файл в браузере
        webbrowser.open(f'file://{os.path.realpath(output_file)}')
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")

# Пример использования
input_file = "C:/Users/newfuf/Desktop/" + input("Введите имя файла с расширением: ")

markdown_to_html(input_file)
