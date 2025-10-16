from pyspark import SparkConf,SparkContext

conf=SparkConf().setAppName('WordCount').setMaster('local[*]')
sc=SparkContext(conf=conf)

n=input('Enter the lines')

lines=sc.parallelize([n])
words=lines.map(lambda x:x.split())

paired_words=words.map(lambda word:(word,1))
word_count=paired_words.reduceByKey(lambda a,b:a+b)
for word,count in word_count.collect():
    print(f'{word}:{count}')
sc.stop()