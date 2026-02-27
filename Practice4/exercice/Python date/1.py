from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Current Date:", current_date)
print("Date 5 Days Ago:", new_date)