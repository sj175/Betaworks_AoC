class Jankyset:
	def __init__(self, some_iterator):
		#Interestingly, the CPython implementation does something similar (but much MUCH smarter than this): https://hg.python.org/releasing/3.6/file/tip/Objects/setobject.c
		#Whereas the OpenJDK just backs a HashSet with a HashMap: https://zgrepcode.com/java/openjdk/10.0.2/java.base/java/util/hashset.java
		self.number_of_buckets = 10 #this is the default number of buckets
		self.buckets = [[] for _ in range(self.number_of_buckets)]
		for x in some_iterator:
			self.add(x)


	def hash(self, item):
		return hash(item) % self.number_of_buckets #hash is built in to Python


	def add(self, element):
		self.buckets[self.hash(element)].append(element)

	def __contains__(self, element):
		return element in self.buckets[self.hash(element)] #this is why contains is actually O(n) in the worst case. If each bucket were a binary search tree we could get this down to O(log n)


	def __eq__(self, other):
		pass

	def __str__(self):
		output = ''
		for bucket in self.buckets:
			output += str(bucket)

		return output
