import os
import django
import pandas as pd
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

# from mysite.models import Post

# posts = Post.objects.all()
# print(posts)

from mysite.models import Country,City
url = "https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html"
raw_data = pd.read_html(url)
time.sleep(3)

data = raw_data[0]
cities = list()
for i in range(len(data)):
	temp = tuple(data['cities'].iloc[i])
	cities.append(temp)

for c in cities:
    cnt =Country.objects.get(country_id =c[2])
    temp = City(name=c[1], country=cnt, population=c[3])
    print(cnt)
    print()
    # temp.save()

cities = City.objects.all()
print(cities)

# country_id = list(data['countries']['id'])
# country_name = list(data['countries']['name'])
# countries = zip(country_id,country_name)
# for country in countries:
# 	temp = Country(name=country[1], country_id=country[0])
# 	temp.save()
# 	print(country)
# countries = Country.objects.all()
# print(countries)
# print("Done!")
