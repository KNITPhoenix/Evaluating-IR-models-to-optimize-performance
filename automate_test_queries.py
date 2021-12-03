import json
import urllib.request
import urllib


def main():
    model_name = 'bm25'
    count = 1

    with open('D:/CSE_535_IR/project3_data/test-queries.txt', encoding="utf-8") as inputfile:
        for line in inputfile:
            input_query = line[4:]
            input_query = input_query.strip('\n').replace(':', '')
            encoded_query = urllib.parse.quote(input_query)
            inurl = 'http://localhost:8983/solr/' + model_name + '/select?fl=id%2Cscore&q=text_en%3A(' \
                    + encoded_query + ')%20or%20text_de%3A(' + encoded_query + ')%20or%20text_ru%3A(' \
                    + encoded_query + ')' + '&rows=20&wt=json'
            #print(inurl1)
            qid = str(count).zfill(3)

            outf = open(str(count) + '.txt', 'a+')
            data = urllib.request.urlopen(inurl).read()
            docs = json.loads(data.decode('utf-8'))['response']['docs']
            rank = 1

            for doc in docs:
                outf.write(str(qid) + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + model_name + '\n')
                o=str(qid) + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + model_name + '\n'
                rank += 1
            outf.close()
            count += 1


if __name__ == '__main__':
    main()