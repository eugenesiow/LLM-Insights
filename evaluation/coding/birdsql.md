# Bird-SQL

BIRD (BIg Bench for LaRge-scale Database Grounded Text-to-SQL Evaluation) represents a cross-domain dataset that examines the impact of extensive database contents on text-to-SQL parsing. BIRD contains over 12,751 question-SQL pairs and 95 big databases with a total size of 33.4 GB. It covers more than 37 professional domains, such as blockchain, hockey, healthcare and education, etc. The benchmark was developed by Li et al. in the paper titled [Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs](https://arxiv.org/abs/2305.03111) and published in Nov 2023.

## Links

* Abstract: https://arxiv.org/abs/2305.03111
* Homepage: https://bird-bench.github.io/
* Code: https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/bird
* Dataset: https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/bird#dataset-introduction
* License: [CC-BY-SA-4.0](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/bird)

## Example Questions

Questions in the BIRD are divided into two main categories. The `Fundamental Type` of questions are comparable to other text-to-SQL benchmarks. The `Reasoning Type` of questions requires external knowledge grounding to answer. Below is a table showing example questions of both main categories and their subcategories.

| Question Type | Sub Type | Question / SQL |
|---|---|---|
| Fundamental Type | Match-based | How many gas stations in CZE has Premium gas? <br> `SELECT COUNT(GasStationID) FROM gasstations WHERE Country = 'CZE' AND Segment = 'Premium'` |
|  | Ranking | What are the titles of the top 5 posts with the highest popularity? <br> `SELECT Title FROM posts ORDER BY ViewCount DESC LIMIT 5` |
|  | Comparison | How many color cards with no borders have been ranked higher than 12000 on EDHRec? <br> `SELECT COUNT(id) FROM cards WHERE edhrecRank > 12000 AND BorderColor = 'borderless'` |
|  | Counting | How many of the members' hometowns are from Maryland state? <br> `SELECT COUNT(T2.member_id) FROM zip_code AS T1 INNER JOIN member AS T2 ON T1.zip_code = T2.zip WHERE T1.state = 'Maryland'` |
|  | Aggregation | What is the average height of the superheroes from Marvel Comics? <br> `SELECT AVG(T1.height_cm) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id WHERE T2.publisher_name = 'Marvel Comics'` |
| Reasoning Type | Domain Knowledge | Name the ID and age of patient with two or more laboratory examinations which show their hematocrit level exceeded the normal range. <br> `SELECT T1.ID, strftime('%Y', CURRENT_TIMESTAMP) - strftime('%Y', T1.birthday) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.ID IN ( SELECT ID FROM Laboratory WHERE HCT > 52 GROUP BY ID HAVING COUNT(ID) >= 2 )` |
|  | Numeric Computation | Among the posts with a score of over 20, what is the percentage of them being owned by an elder user? <br> `SELECT COUNT(T1.ownerUserId * 1.0) * 100.0 / COUNT(T1.id) FROM posts AS T1 INNER JOIN users AS T2 ON T1.ownerUserId = T2.id WHERE T1.Score > 20` |
|  | Synonym | How many clients opened their accounts in Jesenik branch were women? (female) <br> `SELECT COUNT(T1.client_id) FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T1.gender = 'F' AND T2.A2 = 'Jesenik'` |
|  | Value Illustration | Among the weekly issuance accounts, how many have a loan of under 200000? <br> `SELECT COUNT(T1.account_id) FROM loan AS T1 INNER JOIN account AS T2 ON T1.account_id = T2.account_id WHERE T2.frequency = 'POPLATEK TYDNE' AND T1.amount < 200000` |

## Citations

```bibtex
@article{li2024can,
  title={Can llm already serve as a database interface? a big bench for large-scale database grounded text-to-sqls},
  author={Li, Jinyang and Hui, Binyuan and Qu, Ge and Yang, Jiaxi and Li, Binhua and Li, Bowen and Wang, Bailin and Qin, Bowen and Geng, Ruiying and Huo, Nan and others},
  journal={Advances in Neural Information Processing Systems},
  volume={36},
  year={2024}
}
```