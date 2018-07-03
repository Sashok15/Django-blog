import argparse
import psycopg2 as sql

parser = argparse.ArgumentParser(description="Укажите таблицу и количество строк")
parser.add_argument('--namedb', "-nd", type=str)
parser.add_argument('--quantity', "-q", type=int)
options = parser.parse_args()
conn = sql.connect(database='BlogTest', user='postgres',
                   password='root', host='localhost', port=5432)
cursor = conn.cursor()

if options.namedb == 'blog_article':
    for i in range(options.quantity):
        cursor.execute("INSERT INTO blog_article(title, text, author_id) VALUES (%s, %s, %s)",
                       ('article title', 'content, text {0}'.format(i), 1))
elif options.namedb == 'blog_comment':
    for i in range(options.quantity):
        cursor.execute("INSERT INTO blog_comment(article_id, text, author_id) VALUES (%s, %s, %s)",
                       (17, 'content, text {0}'.format(i), 1))
conn.commit()
cursor.close()
conn.close()
