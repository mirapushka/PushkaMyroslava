leads = ["Ivan@GMail.com", "ivan@gmail.com ", " vasya@mail.com", "maryna@urk.net"]
buyers = ["ivan@gmail.com ", "Vasya@mail.com", "max@ukr.net  "]

cleaned_leads = [email.strip().lower() for email in leads]
cleaned_buyers = [email.strip().lower() for email in buyers]

leads_set = set(cleaned_leads)
buyers_set = set(cleaned_buyers)

all_users = leads_set | buyers_set
total_unique_users = len(all_users)

loyal_clients = leads_set & buyers_set

potential_clients = leads_set - buyers_set

buyers_from_webinar = len(loyal_clients)
total_viewers = len(leads_set)

conversion_rate = (buyers_from_webinar / total_viewers) * 100

print(f"Унікальні ліди: {leads_set}")
print(f"Унікальні покупці: {buyers_set}")
print(f"Загальна кількість унікальних користувачів: {total_unique_users}")
print(f"Лояльні клієнти (вебінар + покупка): {loyal_clients}")
print(f"Потенційні клієнти (тільки вебінар): {potential_clients}")
print(f"Конверсія вебінару (Conversion Rate): {conversion_rate:.2f}%")