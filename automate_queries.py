import json
# if you are using python 3, you should
import urllib.request
import urllib
import string

# import urllib2

cores = ['bm25', 'vsm']

def main():
    ls=[]
    for core in cores:
        # change the url according to your own core name and query
        output_file = 'D:/CSE_535_IR/project3_data/output/'+core + '.txt'
        outfile = open(output_file, 'a+')
        counter = 0

        with open('D:/CSE_535_IR/project3_data/queries.txt', encoding="utf-8") as input_file:
            for query in input_file:
                counter += 1
                input_query = query[4:]
                input_query = input_query.strip('\n').replace(':', '')
                encoded_query = urllib.parse.quote(input_query)
                print(encoded_query)
                query_url = 'http://localhost:8983/solr/' + core + '/select?fl=id%2Cscore&q=text_en%3A(' \
                            + encoded_query + ')%20or%20text_de%3A(' + encoded_query + ')%20or%20text_ru%3A(' \
                            + encoded_query + ')' + '&rows=20&wt=json'
                # if you're using python 3, you should use
                data = urllib.request.urlopen(query_url)
                #print(query_url)

                docs = json.load(data)['response']['docs']
                # change query id and IRModel name accordingly
                if counter < 10:
                    qid = '00' + str(counter)
                elif counter > 100:
                    qid = str(counter)
                else:
                    qid = '0' + str(counter)
                # the ranking should start from 1 and increase
                rank = 1
                if(qid=='011'):
                    print(query_url)
                    print(input_query)
                for doc in docs:
                    outfile.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(
                        doc['score']) + ' ' + core + '\n')
                    rank += 1
            input_file.close()
            outfile.close()

if __name__ == '__main__':
    main()