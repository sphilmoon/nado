# nasdaq = ["AAPL", "NFLX", "MRNA"]
# nyse = ["F", "JPMG", "PFZR"]

# print(list(zip(nasdaq, nyse)))

zipped = [('AAPL', 'F'), ('NFLX', 'JPMG'), ('MRNA', 'PFZR')]
# print(list(zip(*zipped)))

nasdaq2, nyse2 = zip(*zipped)
print(nasdaq2)
print(nyse2)