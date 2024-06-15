# Common Crawl

## Introduction

When it comes to using common crawl data for training LLMs there are a few important points to note:
1. **You want the superset of all collections for comprehensiveness:** There are [many collections](#collections) and each collection is labelled something like `CC-MAIN-2013-20` or `CC-MAIN-2019-09`. Each collection is a snapshot of a subset (albeit a large subset) of the internet at that point in time. There might be URL and content overlap between the snapshots, however, the [overlap between each collection](https://commoncrawl.github.io/cc-crawl-statistics/plots/crawloverlap) is relatively small (it goes from near 0% to 25%). So getting the **superset of all the collections will give you a more comprehensive picture** of publicly available web text on the internet. That's probably the base corpus you want to quality filter from for LLM pre-training.
2. **WARC vs WET decisions:** Common crawl releases a [variety of files and formats](#warc-vs-wet) with each collection. One major decision you'll need to make is whether to use WARCs, which have the raw html of each page collected, or WETs, which have just the (best effort) extraction of the webpage body text that common crawl kindly pre-processes for you. If you want the best quality (more cleanly remove the boilerplate of the webpage) you'll want to apply state-of-the-art extraction techniques to WARCs. The **tradeoff here will be the massive size of WARCs**, totalling 5.4PB from 97 collections from 2013 to 2024 - storing and processing becomes a more costly activity as compared to using the 708TB of WETs. 

## File Formats

### WARC vs WET

#### WARC (Web ARChive) Format

[WARC](https://iipc.github.io/warc-specifications/specifications/warc-format/warc-1.0/) is the industry standard for web archiving.  It stores request and response headers, additional metadata, and new record types like resource revisit, metadata, and conversion. It's suitable for large–scale web archiving and supports the archiving of complex digital resources. Common Crawl has used WARC since the `CC-MAIN-2013-20` collection (prior to that the [ARC format](https://commoncrawl.org/errata/arc-format-legacy-crawls) was used).

The header of a document in a WARC file looks something like the example below. For the common crawl datasets, the content is 95% and above of [content-type text/HTML](https://commoncrawl.github.io/cc-crawl-statistics/plots/mimetypes).

```
WARC/1.0
WARC-Type: response
WARC-Date: 2023-11-29T19:37:32Z
WARC-Record-ID: <urn:uuid:c52512d3-8616-40e7-9b2b-095ca5dca5a1>
Content-Length: 77056
Content-Type: application/http; msgtype=response
WARC-Warcinfo-ID: <urn:uuid:369b5ad7-dae0-41c6-9ebd-9fb00aad1e4a>
WARC-Concurrent-To: <urn:uuid:8dc593cc-6eeb-40fc-845d-0726bde5ec2f>
WARC-IP-Address: 31.11.32.54
WARC-Target-URI: https://www.antonaccisrl.it/getidm355/2075meofitems
WARC-Payload-Digest: sha1:2ZPX6XYOT55QZSUEG3ADWH3HYEFRMJAV
WARC-Block-Digest: sha1:M3WLR4GN2BHIWYZDE3GKMHBL6326UWJ6
WARC-Identified-Payload-Type: text/html

HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Server: Microsoft-IIS/8.5
X-Powered-By: ASP.NET
X-Aruba2-Cache: NA
X-Aruba-Cache: NA
Date: Wed, 29 Nov 2023 19:37:32 GMT
Content-Length: 76848
```

The header is followed by the content/body of the response. The WARC file just appends these WARC documents together and they are gzipped up. Since each WARC is multiline and concatanated together, parsing the WARCs requires properly detecting each WARC document. I would highly recommend using a battle-tested library like [warcio](https://github.com/webrecorder/warcio) to iterate over the archive files.

#### WET (Web Extracted Text) Files

These files are part of the Common Crawl dataset and contain extracted plain text from web content.  WET files only contain the body text of web pages, extracted from the HTML and excluding any HTML code, images, or other media.  This makes them useful for text analysis and natural language processing (NLP) tasks.

WET files are ideal for applications where only the text of web pages is needed, such as linguistic analysis, content categorisation, and other text–focused activities.

### CC Index

Each common crawl collection has a corresponding set of indexes, these are in the "ZipNum" CDX format (the same format that is used by the Wayback Machine at the Internet Archive). These indexes are sharded into 300 files, starting from `0` to `299` (e.g `cdx-00299.gz`).

Check out the [CC Indexes](CC_INDEX.md) section to find out more on using them.

## Collections

The following is a list of common crawl collections (or dumps) and the size of the collection's WARC files and WET files. Collections **before** the `CC-MAIN-2013-20` collection are considered [legacy crawl](#legacy-crawls) collections and are not included in this list. 

|#    |Collection Name|WARC Size (in TB)|WET Size (in TB)|
|-----|---------------|-----------------|----------------|
|1    |CC-MAIN-2013-20|23.64            |4.42            |
|2    |CC-MAIN-2013-48|31.93            |3.36            |
|3    |CC-MAIN-2014-10|33.19            |4.01            |
|4    |CC-MAIN-2014-15|37.47            |4.57            |
|5    |CC-MAIN-2014-23|53.89            |6.44            |
|6    |CC-MAIN-2014-35|42.41            |5.18            |
|7    |CC-MAIN-2014-41|44.56            |5.31            |
|8    |CC-MAIN-2014-42|53.71            |6.89            |
|9    |CC-MAIN-2014-49|28.53            |3.55            |
|10   |CC-MAIN-2014-52|32               |3.69            |
|11   |CC-MAIN-2015-06|27.91            |3.21            |
|12   |CC-MAIN-2015-11|28.12            |3.26            |
|13   |CC-MAIN-2015-14|25.13            |2.92            |
|14   |CC-MAIN-2015-18|33.27            |3.74            |
|15   |CC-MAIN-2015-22|31.58            |3.58            |
|16   |CC-MAIN-2015-27|26.27            |2.99            |
|17   |CC-MAIN-2015-32|28.84            |3.25            |
|18   |CC-MAIN-2015-35|29.49            |3.15            |
|19   |CC-MAIN-2015-40|21.13            |2.25            |
|20   |CC-MAIN-2015-48|29.64            |3.11            |
|21   |CC-MAIN-2016-07|28.57            |4.59            |
|22   |CC-MAIN-2016-18|20.82            |3.42            |
|23   |CC-MAIN-2016-22|22.95            |3.73            |
|24   |CC-MAIN-2016-26|19.02            |3.12            |
|25   |CC-MAIN-2016-30|29.32            |4.61            |
|26   |CC-MAIN-2016-36|26.78            |4.23            |
|27   |CC-MAIN-2016-40|28.94            |4.54            |
|28   |CC-MAIN-2016-44|53.18            |8.65            |
|29   |CC-MAIN-2016-50|49.35            |8.19            |
|30   |CC-MAIN-2017-04|53.95            |8.97            |
|31   |CC-MAIN-2017-09|55.88            |9.14            |
|32   |CC-MAIN-2017-13|60.74            |9.3             |
|33   |CC-MAIN-2017-17|59.03            |8.95            |
|34   |CC-MAIN-2017-22|57.98            |8.95            |
|35   |CC-MAIN-2017-26|63.33            |9.44            |
|36   |CC-MAIN-2017-30|57.62            |8.19            |
|37   |CC-MAIN-2017-34|65.14            |9.81            |
|38   |CC-MAIN-2017-39|59.13            |8.86            |
|39   |CC-MAIN-2017-43|84.9             |10.58           |
|40   |CC-MAIN-2017-47|66.17            |9.06            |
|41   |CC-MAIN-2017-51|61.2             |8.41            |
|42   |CC-MAIN-2018-05|74.33            |9.29            |
|43   |CC-MAIN-2018-09|71.96            |9.62            |
|44   |CC-MAIN-2018-13|67.66            |8.8             |
|45   |CC-MAIN-2018-17|54.24            |8.4             |
|46   |CC-MAIN-2018-22|51.61            |7.59            |
|47   |CC-MAIN-2018-26|56.58            |8.37            |
|48   |CC-MAIN-2018-30|61.07            |9.08            |
|49   |CC-MAIN-2018-34|67.79            |6.92            |
|50   |CC-MAIN-2018-39|47.9             |7.87            |
|51   |CC-MAIN-2018-43|58.84            |8.22            |
|52   |CC-MAIN-2018-47|54.16            |7.42            |
|53   |CC-MAIN-2018-51|65.31            |8.43            |
|54   |CC-MAIN-2019-04|58.86            |7.98            |
|55   |CC-MAIN-2019-09|59.86            |7.62            |
|56   |CC-MAIN-2019-13|49.09            |7.47            |
|57   |CC-MAIN-2019-18|44.86            |6.96            |
|58   |CC-MAIN-2019-22|51.48            |7.7             |
|59   |CC-MAIN-2019-26|49.42            |7.59            |
|60   |CC-MAIN-2019-30|46.1             |7.8             |
|61   |CC-MAIN-2019-35|53.53            |9.29            |
|62   |CC-MAIN-2019-39|55.99            |8.16            |
|63   |CC-MAIN-2019-43|59.56            |9.94            |
|64   |CC-MAIN-2019-47|53.95            |8.34            |
|65   |CC-MAIN-2019-51|47.47            |8.06            |
|66   |CC-MAIN-2020-05|59.94            |10              |
|67   |CC-MAIN-2020-10|49.28            |7.97            |
|68   |CC-MAIN-2020-16|62.67            |8.97            |
|69   |CC-MAIN-2020-24|53.16            |8.42            |
|70   |CC-MAIN-2020-29|62.64            |9.87            |
|71   |CC-MAIN-2020-34|48.9             |7.56            |
|72   |CC-MAIN-2020-40|81.8             |10.28           |
|73   |CC-MAIN-2020-45|63.79            |8.23            |
|74   |CC-MAIN-2020-50|59.95            |7.89            |
|75   |CC-MAIN-2021-04|78.98            |10.04           |
|76   |CC-MAIN-2021-10|62.51            |8.06            |
|77   |CC-MAIN-2021-17|69.78            |9.25            |
|78   |CC-MAIN-2021-21|66.17            |7.65            |
|79   |CC-MAIN-2021-25|57.9             |7.24            |
|80   |CC-MAIN-2021-31|75.34            |9.43            |
|81   |CC-MAIN-2021-39|72.16            |8.7             |
|82   |CC-MAIN-2021-43|85.11            |9.79            |
|83   |CC-MAIN-2021-49|68.66            |7.18            |
|84   |CC-MAIN-2022-05|73.5             |8.63            |
|85   |CC-MAIN-2022-21|92.81            |9.8             |
|86   |CC-MAIN-2022-27|84.08            |8.97            |
|87   |CC-MAIN-2022-33|68.95            |7.24            |
|88   |CC-MAIN-2022-40|82.71            |9.11            |
|89   |CC-MAIN-2022-49|92.59            |9.58            |
|90   |CC-MAIN-2023-06|88.02            |9.05            |
|91   |CC-MAIN-2023-14|87.95            |8.74            |
|92   |CC-MAIN-2023-23|86.77            |8.69            |
|93   |CC-MAIN-2023-40|98.38            |9.3             |
|94   |CC-MAIN-2023-50|99.25            |9.3             |
|95   |CC-MAIN-2024-10|90.36            |8.4             |
|96   |CC-MAIN-2024-18|81.71            |7.54            |
|97   |CC-MAIN-2024-22|78.62            |7.31            |
|**Total**|               |**5432.77**        |**708.73**          |


### Legacy Crawls

Legacy crawl collections are archived in the ARC format instead of WARC format and cannot be comprehensively extracted with most available software today. Below is a list of the crawls.

|#  |Legacy Crawl Name|
|---|-----------------|
|1  |CC-MAIN-2008-2009|
|2  |CC-MAIN-2009-2010|
|3  |[CC-MAIN-2012](https://commoncrawl.org/blog/2012-crawl-data-now-available)     |