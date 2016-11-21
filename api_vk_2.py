def messages_get_history(user_id, offset=0, count=200):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "user_id must be positive integer"
    assert count >= 0, "user_id must be positive integer"
    import requests
    domain = "https://api.vk.com/method"
    access_token = '2f2dc3b5e40241ab92704ee25d69908bebafcc3a9d9ffa5f341bdbe8709d70d47b5345ebfac8dd622b97f'
    user_id = user_id
    count = count
    offset = offset

    query_params = {
        'domain': domain,
        'access_token': access_token,
        'user_id': user_id,
        'count': count,
        'offset': offset
    }

    query = "{domain}/messages.getHistory?user_id={user_id}&count={count}&offset={offset}&access_token={access_token}&v=5.53".format(
        **query_params)
    response = requests.get(query)
    messages_list = []
    if response.json()['response']['count'] < 200:
        count_messages = response.json()['response']['count']
    else:
        count_messages = count
    for i in range(count_messages):
        messages_list.append(response.json()['response']['items'][i])
    return messages_list
messages = messages_get_history(209526270)


from collections import Counter
from operator import itemgetter
from datetime import datetime


def count_dates_from_messages(messages):
    dates = []
    for item in messages:
        dates.append(datetime.fromtimestamp(item['date']).strftime("%Y-%m-%d"))
    dates_counter = Counter(dates)
    items = list(dates_counter.items())
    items.sort(key=itemgetter(0))
    dates_new = []
    counts = []
    for item in items:
        dates_new.append(item[0])
        counts.append(item[1])
    return dates_new, counts
print(count_dates_from_messages(messages))

import plotly
plotly.tools.set_credentials_file(username='AlexandraFr', api_key='jn6rgmst7q')
import plotly.plotly as py
import plotly.graph_objs as go


dates = count_dates_from_messages(messages)[0]
counts = count_dates_from_messages(messages)[1]
data = [go.Scatter(x = dates, y = counts)]
py.iplot(data)
