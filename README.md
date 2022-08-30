# MySQLByPassForSafeDog / MySQL注入绕安全狗Tamper

## Code By:Tas9er @A.E.0.S Security Team

######################################################################## 

##### :x:风险概述:

本工具仅限授权安全测试使用,禁止非法攻击未授权站点



##### :ballot_box_with_check:使用教程

此Tamper仅仅适用于MySQL数据库

在SQLMap使用过程中添加参数--tamper=MySQLByPassForSafeDog



##### :trident:绕过测试

(安全狗公司真的业内良心，免费产品都保持渐进式更新，我都看哭了)

安装网站安全狗Apache最新版

![01](/image/01.jpg)



启用安全狗，不加MySQLByPassForSafeDog绕狗Tamper:

python sqlmap.py -u "http://192.168.2.3:60001/sqli.php?id=1" --random-agent --dbms=mysql

![2](/image/2.jpg)



启用安全狗，添加MySQLByPassForSafeDog绕狗Tamper:

python sqlmap.py -u "http://192.168.2.3:60001/sqli.php?id=1" --random-agent --dbms=mysql --tamper=MySQLByPassForSafeDog

![3](/image/3.jpg)



##### :100:绕过POC

可以添加参数-v 3进行学习查看

python sqlmap.py -u "http://192.168.2.3:60001/sqli.php?id=1" --random-agent --dbms=mysql --tamper=MySQLByPassForSafeDog -v 3

![4](/image/4.jpg)



##### 问题反馈

别你🐴天天问东问西，有bug有想法自己想办法。

