# Scrapy-news

[Scrapy](https://docs.scrapy.org/en/latest/index.html) spiders for news website


# 1. How to use

1. Install dependency (`pip install -r requirements.txt`)
2. Run spider
3. Modify [Scrapy Settings](https://docs.scrapy.org/en/latest/topics/settings.html) if needed

```
scrapy runspider [SPIDER PATH] -a start_id=1000 -a end_id=1500 -o [OUTPUT_FILE]
```

## 1.1 Example

```bash
scrapy runspider ./news/spiders/prachatai.py -a start_id=1000 -a end_id=1500 -o prachatai.jl
```

# 2. Spiders

## 2.1 Prachatai

URL: https://prachatai.com/print/[ARTICLE_ID]

** Arguments **:
- `start_id` - Article IDs
- `end_id` - Article IDs 

```bash
scrapy runspider ./news/spiders/prachatai.py -a start_id=1000 -a end_id=1500 -o prachatai.jl
```

## 2.2 Thaipbs

URL: http://news.thaipbs.or.th/content/[ARTICLE_ID]

** Arguments **:
- `start_id` - Article IDs
- `end_id` - Article IDs 

```bash
scrapy runspider ./news/spiders/thaipbs.py  -a start_id=1000 -a end_id=1500 -o thaipbs.jl
```

# 3. Output format

Support as scrapy [feed export](https://docs.scrapy.org/en/latest/topics/feed-exports.html?highlight=output)

- `.csv`
- `.jl` (JSON Line)
- `.json`
- `.xml`

```bash
scrapy runspider .news/spiders/thaipbs.py  -a start_id=1000 -a end_id=1500 -o thaipbs.csv
```