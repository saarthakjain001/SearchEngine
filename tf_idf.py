#!/usr/bin/env python
import math
class tf_idf:
	def tf_doc_specific(self,myList,global_word):
		word_count = {}
		for word in myList:
			if word in word_count:
				word_count[word] = word_count[word]+1;
			else :
				word_count[word] = 1;
		for word in word_count:
			count = word_count[word]
			word_count[word]=float(1+math.log(count,10));
		return_vector = []
		for word in global_word:
			if word in word_count:
				return_vector.append(word_count[word]);
			else:
				return_vector.append(0);
		iterate=0;
		for word in global_word:
			print(word + ' ' + str(return_vector[iterate]))
			iterate=iterate+1
		return return_vector

globa = ['Wishing','former', 'cricketer', 'Zaheer', 'Khan', 'on', 'the', 'occasion', 'of', 'his', '41st', 'birthday', 'Team', 'India', 'all-rounder' ,'Hardik', 'Pandya', 'shared', 'a', 'video', 'him','trolls','the fuck']
test = ['Wishing','former', 'cricketer', 'Zaheer', 'Khan', 'on', 'the', 'occasion', 'of', 'his', '41st', 'birthday', 'Team', 'India', 'all-rounder' ,'Hardik', 'Pandya', 'shared', 'a', 'video', 'of', 'him','Pandya','Pandya','trolls','Zaheer','Khan']

tr = tf_idf()
tr.tf_doc_specific(test,globa)
