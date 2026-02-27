#. datetime
from datetime import datetime, date, time, timedelta
d = date(2026, 2, 27)
now = datetime.now()
utc = datetime.utcnow()
#.  Форматирование
now.strftime("%Y-%m-%d %H:%M:%S")
'''.
%Y — год
%m — месяц
%d — день
%H — часы
%M — минуты
%S — секунды
'''
#.  Парсинг строки
datetime.strptime("2026-02-27", "%Y-%m-%d")
#.  timedelta
tomorrow = datetime.now() + timedelta(days=1)
#.   Работа с временными зонами
from datetime import timezone
datetime.now(timezone.utc)
#.  timestamp
datetime.fromtimestamp(1700000000)
#.  calendar
import calendar
calendar.month(2026, 2)