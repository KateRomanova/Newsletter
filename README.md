Cервис управления рассылками, администрирования и получения статистики. 
Используется для информирования и привлечения клиентов.

Для корректной работы приложения необходимо установить следующие зависимости:

[tool.poetry.dependencies]
python = "^3.12"
psycopg2-binary = "^2.9.9"
black = "^24.4.2"
django = "4.2.2"
ipython = "^8.26.0"
django-crontab = "^0.7.1"
redis = "^5.0.8"
python-dotenv = "^1.0.1"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"