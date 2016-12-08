class AvgNumWords(object):

  def get_avg(self):
    with open('text.txt') as f1:
      sen = f1.readlines()
      list_a = map(lambda s: self.advanced_strip(s.strip()), sen)
      avg_it = self.average_len(list_a)
      print str(round(avg_it))[:-2]

  def advanced_strip(self, line_space):
    return line_space.strip(", ")

  def average_len(self, list_a):
    a = [len(i.split()) for i in list_a]
    return 0 if len(a) == 0 else (float(sum(a)) / len(a))

def main():
  avg_num = AvgNumWords()
  avg_num.get_avg()


if __name__ == "__main__":
    main()


