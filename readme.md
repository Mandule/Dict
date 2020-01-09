# 词形还原

## 环境
* python3.7

## 字典数据
* dict.txt：dic_ec.txt 编码转换后的文件。
* dict_noun.txt：网络爬虫爬取的名词还原字典。
* dict_verb.txt：网络爬虫爬取的动词还原字典。

##  基于词典的词形还原算法
* 通过[维基词典](https://zh.wiktionary.org/wiki/%E9%99%84%E5%BD%95:%E8%8B%B1%E8%AF%AD%E4%B8%8D%E8%A7%84%E5%88%99%E5%A4%8D%E6%95%B0)爬取英语不规则复数变换表。
* 通过[百度百科](https://baike.baidu.com/item/%E8%8B%B1%E8%AF%AD%E4%B8%8D%E8%A7%84%E5%88%99%E5%8A%A8%E8%AF%8D%E8%A1%A8/1619648?fr=aladdin)爬取英语不规则动词变换表。
* 创建三个字典：原始字典 all ，不规则名词词典 noun ，不规则动词词典 verb 。
* 用户输入 W。
* 若 W 存在于 all 中，则直接输出 W 和 all 中 W 对应的 value。
* 若 W 不存在于 all 中，则判断 W 是否存在于 noun中。
* 若 W 存在于 noun 中，则输出 W 和其还原后的词形 W ’，和 all 中 W ' 对应的 value。
* 若 W 不存在于 noun中，则判断 W 是否存在于 verb 中。
* 若 W 存在于verb 中， 则输出 W 和其还原后的词形 W ’，和 all 中 W ' 对应的 value。
* 若 W 不存在于verb中，则输出 W 和按规则还原后的词形 W ’，和 all 中 W ' 对应的 value。
* 如果以上任何一种对 W 的处理得到 W ’ 后，W ‘ 不存在于all 中，则输出<未登录词模块>。