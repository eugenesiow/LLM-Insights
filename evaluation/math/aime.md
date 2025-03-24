# AIME

AIME stands for the [American Invitational Mathematics Examination](https://maa.org/maa-invitational-competitions/). The American Invitational Mathematics Examination (AIME) is the second exam in the series of exams used to challenge bright students on the path toward choosing the team that represents the United States at the International Mathematics Olympiad (IMO). 

AIME is a selective 15-question, 3-hour test given since 1983 to those who rank in the top 5% on the [American Mathematics Competition (AMC)](https://en.wikipedia.org/wiki/American_Mathematics_Competitions) 12 high school mathematics examination (formerly known as the AHSME), and starting in 2010, those who rank in the top 2.5% on the AMC 10. The AMC 10 is for students under the age of 17.5 and in grades 10 and below while the AMC 12 is for students under the age of 19.5 and in grades 12 and below. The 15 questions are ordered based on increasing difficulty, cover a wide range of mathematical topics, including algebra, geometry, and number theory, with the answer to every question being a single integer from 0 to 999. The median (human) score is historically between 4 and 6 questions correct (out of the 15 possible). Two versions of the test (AIME I and AIME II) are given every year (so there are 30 questions total). 

AIME 2024 (AIME24) was released in February 2024, while AIME25 was released in February 2025.

## Links

* Homepage: https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions
* Code: https://github.com/GAIR-NLP/AIME-Preview
* Dataset: https://huggingface.co/datasets/math-ai/aime24 (2024), https://huggingface.co/datasets/math-ai/aime25 (2025)
* Dataset: https://github.com/GAIR-NLP/AIME-Preview/blob/main/eval/data/aime/test2024.jsonl (w/ solutions)
* License: According to [AoPS](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I), the AIME problems are copyrighted by the [Mathematical Association of America](http://www.maa.org/)'s [American Mathematics Competitions](https://maa.org/student-programs/amc/).

## Example Questions

Below are 2 example questions from AIME24.

<details>
<summary>Problem 1 - with crowdsourced solutions</summary>

Problem: Every morning Aya goes for a $9$-kilometer-long walk and stops at a coffee shop afterwards. When she walks at a constant speed of $s$ kilometers per hour, the walk takes her 4 hours, including $t$ minutes spent in the coffee shop. When she walks $s+2$ kilometers per hour, the walk takes her 2 hours and 24 minutes, including $t$ minutes spent in the coffee shop. Suppose Aya walks at $s+\frac{1}{2}$ kilometers per hour. Find the number of minutes the walk takes her, including the $t$ minutes spent in the coffee shop.

Solution 1: $\frac{9}{s} + t = 4$ in hours and $\frac{9}{s+2} + t = 2.4$ in hours.<br>Subtracting the second equation from the first, we get, <br>$\frac{9}{s} - \frac{9}{s+2} = 1.6$<br>Multiplying by $(s)(s+2)$, we get <br>$9s+18-9s=18=1.6s^{2} + 3.2s$<br>Multiplying by 5\/2 on both sides, we get<br>$0 = 4s^{2} + 8s - 45$<br>Factoring gives us <br>$(2s-5)(2s+9) = 0$, of which the solution we want is $s=2.5$.<br>Substituting this back to the first equation, we can find that $t = 0.4$ hours.<br>Lastly, $s + \frac{1}{2} = 3$ kilometers per hour, so<br>$\frac{9}{3} + 0.4 = 3.4$ hours, or $\boxed{204}$ minutes<br>-Failure.net

Solution 2: The amount of hours spent while walking on the first travel is $\frac{240-t}{6}$. Thus, we have the equation $(240-t)(s) = 540$, and by the same logic, the second equation yields $(144-t)(s+2) = 540$. We have $240s-st = 540$, and $288+144s-2t-st = 540$. We subtract the two equations to get $96s+2t-288 = 0$, so we have $48s+t = 144$, so $t = 144-48s$, and now we have $(96+48s)(s) = 540$. The numerator of $s$ must evenly divide 540, however, $s$ must be less than 3. We can guess that $s = 2.5$. Now, $2.5+0.5 = 3$. Taking $\frac{9}{3} = 3$, we find that it will take three hours for the 9 kilometers to be traveled. The t minutes spent at the coffeeshop can be written as $144-48(2.5)$, so t = 24. $180 + 24 = 204$.<br>-sepehr2010

Answer: 204
</details>

<details>
<summary>Problem 2 - just answer</summary>

Problem: Let $ABC$ be a triangle inscribed in circle $\omega$. Let the tangents to $\omega$ at $B$ and $C$ intersect at point $D$, and let $\overline{AD}$ intersect $\omega$ at $P$. If $AB=5$, $BC=9$, and $AC=10$, $AP$ can be written as the form $\frac{m}{n}$, where $m$ and $n$ are relatively prime integers. Find $m + n$.

Answer: 113
</details>

## Implementation

NOTE: See the GAIR-NLP implementation (unofficial) of the task: https://github.com/GAIR-NLP/AIME-Preview/blob/main/eval/eval.py.
