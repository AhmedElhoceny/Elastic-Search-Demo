from elasticsearch import Elasticsearch

client = Elasticsearch(
  "https://6f4c2112090344c4918f971780e345a7.us-central1.gcp.cloud.es.io:443",
  api_key=""
)

info = client.info()
print(info)

documents = [
  { "index": { "_index": "search-tests", "_id": "9780553351927"}},
  {"name": "Snow Crash", "author": "Neal Stephenson", "release_date": "1992-06-01", "page_count": 470, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": True},
  { "index": { "_index": "search-tests", "_id": "9780441017225"}},
  {"name": "Revelation Space", "author": "Alastair Reynolds", "release_date": "2000-03-15", "page_count": 585, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": True},
  { "index": { "_index": "search-tests", "_id": "9780451524935"}},
  {"name": "1984", "author": "George Orwell", "release_date": "1985-06-01", "page_count": 328, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": True},
  { "index": { "_index": "search-tests", "_id": "9781451673319"}},
  {"name": "Fahrenheit 451", "author": "Ray Bradbury", "release_date": "1953-10-15", "page_count": 227, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": True},
  { "index": { "_index": "search-tests", "_id": "9780060850524"}},
  {"name": "Brave New World", "author": "Aldous Huxley", "release_date": "1932-06-01", "page_count": 268, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": True},
  { "index": { "_index": "search-tests", "_id": "9780385490818"}},
  {"name": "The Handmaid's Tale", "author": "Margaret Atwood", "release_date": "1985-06-01", "page_count": 311, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": True},
]

client.bulk(operations=documents, pipeline="ent-search-generic-ingestion")


searchResult = client.search(index="search-tests", q="author")

print(searchResult)
