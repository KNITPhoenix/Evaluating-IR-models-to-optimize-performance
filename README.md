# Evaluating-IR-models-to-optimize-performance-
The goal of this project is to implement various IR models, evaluate the IR system and improve the search result based on your understanding of the models, the implementation and the evaluation.
The dataset given is twitter data in three languages - English, German and Russian, 15 sample queries and the corresponding relevance judgements. You will index the given twitter data using Solr, implement Vector Space Model and BM25 based on Solr, and evaluate the two sets of results using Trec_Eval program. Based on the evaluation result, you are asked to programatically improve the performance in terms of the measure Mean Average Precision (MAP).
Following is the structure of the project. The project uses Solr to produce inverted index and further scoring the documents to build the entire architecture of the search engine and helped in evaluating the performance.
![alt text](https://github.com/KNITPhoenix/Evaluating-IR-models-to-optimize-performance-/main/architecture.jpg?raw=true)

The data given is Twitter data saved in json format, train.json. Three languages are included
- English (text_en), German (text_de) and Russian (text_ru).

**Index**
In this step, we will need to index the data.

**Various IR models**
In this step, you will need to implement Vector Space Model (VSM) and BM25 (Note that Solr
version 6.0 and above by default uses BM25 model). In Solr, these models are implemented
through a predefined class called “Similarity”.
Here are some useful links for your reference:
● All similarity classes that you can choose from Solr, which means that very likely you do
NOT need to implement an IR model from scratch:
https://lucene.apache.org/core/7_7_3/core/org/apache/lucene/search/similarities/package-sum
mary.html
● To specify and customize different similarity functions in Solr Schema:
● https://solr.apache.org/guide/7_5/other-schema-elements.html#similarity

**Input Queries**
You are provided with 15 sample queries (queries.txt) and corresponding manually judged
relevance score (qrel.txt).
queries.txt, includes 15 sample queries. One query per line. Each line has the following
format:
query_number query_text
For example,
001 Russia's intervention in Syria
Your retrieval result is mainly based on the query_text.
qrel.txt, includes manually judged relevance score. Format is as shown
below query_number 0 document_id relevance
For example,
001 0 653278482517110785 0

**Query result of Solr**
The query result of Solr can be specified into json format, which include at least tag: id and
score.

The query result should be processed into below format to accommodate the input format of
TREC evaluation program. A Python script (json_to_trec.py) is provided to help you
accomplish this task.
The final result of the search system should be a ranked list of documents as returned by the
retrieval system. It should have the following format,
query-number Q0 tweet_id rank similarity_score model_name
For example,
001 Q0 653278466788487168 0 0.22385858 default
where,
001 is the query number;
Q0 is a constant, ignored in TREC evaluation;
653278466788487168 is the document id. In this case, tweet_id;
0 is the rank of this document for query 001;
0.22385858 is the similarity score returned by IR model BM25, which is default in
Lucene; default is the model name you used.
A sample file is provided in file sample_trec_input.txt.
NOTE: For final submission, we ask you to restrict the (maximum) number of returned
documents as 20, i.e., in each query url, add “rows=20”.
**
Section 3: TREC Evaluation**
[provided files: qrel.txt, sample_trec_output]
In this part, you will be using TREC_eval program. You can download the latest version from
http://trec.nist.gov/trec_eval/. After downloading, read the README file carefully. One of the
basic commands is
trec_eval -q -c -M1000 official_qrels submitted_results
For example, you can use following command to evaluate the sample query output file.
trec_eval -q -c -M 1000 qrel.txt sample_trec_input.txt
This command will give you a number of common evaluation measure results.
For more information on how to use or interpret the result, go to
http://www-nlpir.nist.gov/projects/t01v/trecvid.tools/trec_eval_video/A.READM
E A sample TREC_eval output file is provided in file sample_trec_output.txt.

**Section 4: Improving the IR system**
Together with your training queries, query results, ground truth judgements and the TREC_eval
result, by now you might gain an intuition on the performance of your IR system. We choose the
measure MAP as main objective to improve. Here is a list of things you could try to improve
your evaluation score.
1. Understand the measure itself. How to improve MAP?
2. Do you need to do advanced query processing to improve the result? For example,
boosting the query based on different fields? Expand the query, say translate the query
into other languages? Use different query parser? Use any filters for query processing?
More details can be found in
https://solr.apache.org/guide/7_5/the-standard-query-parser.html
3. Do you need to have better index? For example, do you need to have additional fields to
use additional analyzer and tokenizer to achieve better query result? For example,
http://wiki.apache.org/solr/SolrRelevancyFAQ#How_can_I_make_exact
case_matches_score_higher
4. Do you need to tweak the parameters of the IR model to make it more suitable to the
query? For example, in BM25 model, there are two parameters you can set up. What is
the meaning of these parameters and how to tweak it?

**FAQs and Tips:**
1. In this project, as you work and play with Solr, you may need to refer to Solr Reference
Guide frequently to complete your tasks.
2. For windows, to install TREC on your machine, follow these steps:
a. install cygwin
b. unzip trec_eval zip file
c. move to trec_eval folder in cygwin terminal and execute make, and you will be
good to go
3. For macOS, if you encounter the following error when installing trec_eval:
invalid active developer path
(/Library/Developer/CommandLineTools), missing xcrun
at: /Library/Developer/CommandLineTools/usr/bin/xcrun
Refer to https://apple.stackexchange.com/questions/254380/macos-mojave-invalid
active-developer-path for more details.
4. For macOS, if you encounter the following error when running trec_eval:
trec_eval: command not found
Refer to
https://www.reddit.com/r/informationretrieval/comments/58luyt/need_help_running_the_
t rec_eval_program/ for a solution.
5. Should I work with schema or schema-less mode?
- You can either work with or without schema, the performance won’t be different.
6. Which Solr version should I use?
- You can use any version above 6.0 as you prefer.
