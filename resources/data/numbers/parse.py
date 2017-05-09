import os
import sys
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup

h = HTMLParser()
target_path = '../../history/numbers'
length_dict = {
  'taiwan_lottery_638': (6, 1),
  'big_lottery_649': (6, 1),
  'today_lottery_539': (5, 0),
  'power_lottery_638': (6, 1),
  # 'dafu_lottery_740': (7, 1),
}

def print_help():
  print 'Usage:'
  print 'python parse.py lottery_type_name'
  print 'ex: python parse.py big_lottery_649'

def ft_int(word):
  try:
    return int(word.strip())
  except:
    # TODO replace all non-digits characters
    return int(word.strip()[1:])

def get_html_table_data(rows):
  data = []
  for row in rows:
    raw_data = [h.unescape(d.text) for d in row.findAll('td')]
    row = raw_data[:1]
    row.extend(raw_data[1].split('/'))
    row = map(ft_int, row)
    row.extend(map(ft_int, raw_data[3:]))
    data.append(row)
  return data

def process(f, length, sn, global_index):
  html = open(f).read()
  soup = BeautifulSoup(html)
  rows = soup.findAll('tr')
  raw_data = get_html_table_data(rows[1:])

  index = 1
  data = []
  for row in raw_data:
    dates = row[:3]
    numbers = row[3:3+length+sn]
    sorted_numbers = numbers[:length]
    sorted_numbers.sort()
    heads = [d/10 for d in numbers[:-sn]]
    heads = [heads.count(d) for d in range(0, 5)]
    ends = [d%10 for d in numbers[:-sn]]
    ends = [ends.count(d) for d in range(0, 10)]
    serial = '%03d%06d' % (dates[0] - 1911, index)

    row = [global_index]
    row.extend(dates)
    row.extend(numbers)
    row.extend(sorted_numbers)
    row.extend(heads)
    row.extend(ends)
    row.append(serial)
    data.append(row)

    index += 1
    global_index += 1
  return data, global_index

def data2csv(headers, data, fn):
  fh = open(fn, 'w')

  fh.write(','.join(headers))
  fh.write('\n')

  for row in data:
    fh.write(','.join(map(str, row)))
    fh.write('\n')
  fh.flush()
  fh.close()

def main(lottery_names):
  folders = os.listdir(target_path)
  for name in lottery_names:
    if name not in folders:
      continue

    length, sn = length_dict[name]
    path = os.path.join(target_path, name)
    files = os.listdir(path)
    files.sort()

    headers = ['index']
    headers.extend(['year', 'month', 'day'])
    headers.extend(map(lambda x: 'raw%d' % x, range(1, length+1)))
    if sn == 1:
      headers.append('special')
    headers.extend(map(lambda x: 'sort%d' % x, range(1, length+1)))
    headers.extend(map(lambda x: 'head%d' % x, range(0, 5)))
    headers.extend(map(lambda x: 'tail%d' % x, range(0, 10)))
    headers.append('serial_number')

    index = 1
    history_data = []
    for f in files:
      data, index = process(os.path.join(path, f), length, sn, index)
      history_data.extend(data)
    data2csv(headers, history_data, '%s.csv' % name)

if __name__ == '__main__':
  if len(sys.argv) == 1:
    print_help()
    exit(0)

  main(sys.argv[1:])
