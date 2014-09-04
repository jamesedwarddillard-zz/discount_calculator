def discount_calc(item_cost, relative_discount, absolute_discount):
	relative_discount_dollars = (relative_discount/100.0) * item_cost
	#confirm that discounts aren't punative (no negative discounts)
	if relative_discount_dollars < 0:
		raise ValueError("No negative discounts here!")
	if absolute_discount < 0:
		raise ValueError("No negative discounts here!")

	discounted_item_cost = item_cost - (relative_discount_dollars + absolute_discount)

	#make sure price doesn't go below zero
	if discounted_item_cost < 0: 
		discounted_item_cost = 0
		return discounted_item_cost
	else: 
		return discounted_item_cost



def main():
	cost = discount_calc(100, -10, 0)
	print "After discounts, your total will be ${}.".format(cost)

if __name__ == "__main__":
	main()