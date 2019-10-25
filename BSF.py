from collections import deque

graph = {}
graph['you'] = ['hari', 'nandan', 'ashok']
graph['hari'] = ['nagraj', 'ramya']
graph['ashok'] = ['aishwarya', 'shiva']
graph['nandan'] = []
graph['nagraj'] = []
graph['ramya'] = []
graph['aishwarya'] = []
graph['shiva'] = []



def person_is_seller(person):
	return person[-1] == 'j'


def breadth_first_search(name):
	search_queue = deque()
	search_queue += graph[name]
	print(search_queue)
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person): 
				return person + ' is a mango seller'
			else:
				search_queue += graph[person]
				print(search_queue)
				searched.append(person)

	return False

print(breadth_first_search('you'))