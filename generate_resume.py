#!/usr/bin/env python3
import yaml
from jinja2 import Environment, FileSystemLoader

# Загружаем данные из resume.yaml
with open("resume.yaml", "r", encoding="utf-8") as file:
    resume_data = yaml.safe_load(file)

# Настраиваем Jinja2
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("neobrutalism.html.j2")

# Рендерим шаблон с данными
html_content = template.render(**resume_data)

# Сохраняем результат в файл
with open("resume.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Резюме сгенерировано в resume.html!")
