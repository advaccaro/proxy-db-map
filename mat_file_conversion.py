#load .mat file, extract relevant data, and 
import scipy.io as sio
import pdb

mat_contents = sio.loadmat('pages2k_hadcrut4_noDetrend_normal_1_9_0.mat')
B = mat_contents['pages2k']

list_of_dicts = list()
#list_of_keys = list()
#dict_of_headers = dict()

#define headers
headers = ['index','archive','latitude','longitude','yearMin','yearMax']
#for head in headers:
#	list_of_keys.append(head)

#retrieve relevant data for each proxy record
for i in range(0,len(B['archive'][0][0][0])):
	list_of_proxy = list()
	index = i + 1
	list_of_proxy.append(index) #index
	list_of_proxy.append(B['archive'][0][0][0][i][0]) #archive type
	list_of_proxy.append(B['loc'][0][0][i][1]) #latitude
	list_of_proxy.append(B['loc'][0][0][i][0]) #longitude
	list_of_proxy.append(B['yearMin'][0][0][i][0]) #minimum year
	list_of_proxy.append(B['yearMax'][0][0][i][0]) #maximum year
	dict_of_proxy = dict(zip(headers,list_of_proxy)) #create proxy dictionary
	list_of_dicts.append(dict_of_proxy) #add proxy dictionary to list of proxy dicts


#pdb.set_trace()

#write to new csv file
fout = open('pages2k_proxy_db_1_9_0.csv','w')
for head in headers:
	fout.write(head + ',')
fout.write('\n')
for dictionary in list_of_dicts:
	for head in headers:
		fout.write(str(dictionary[head]) + ',')
	fout.write('\n')
fout.close()
