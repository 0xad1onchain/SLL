class Sentence:
	lst = []
	# sent = ""
	def __init__ (self,sent):
		self.sent = sent
	def reverse(self):
		ls = self.sent.split()
		rs = ' '.join(i for i in (ls[::-1]))
		self.lst.append(rs)
	def print_rev(self):
		dict = {}
		for i in self.lst:
			vc = 0
			for j in i:
				if j in "aeiou":
					vc=vc+1 
			dict[i] = vc
		print(sorted(dict.items(),key = lambda t:t[1],reverse=True))		


s = input("Enter string 1")
a = Sentence(s)
a.reverse()
s = input("Enter string 2")
b = Sentence(s)
b.reverse()
s = input("Enter string 3")
c = Sentence(s)
c.reverse()
c.print_rev()