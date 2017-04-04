copies = 60
retail_price = 24.95
wholesale_discount = .4 # percentage off from retail_price
upfront_printing_cost = 3 # on etime cost of printing
per_extra_copy = .75 # per copy cost for each additional copy after 1

total_book_cost = (retail_price * (1 - wholesale_discount) * copies) + upfront_printing_cost + (per_extra_copy * (copies-1))
print(round (total_book_cost, 2))
