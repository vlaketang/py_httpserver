
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

print("Content-type:text/html\n")#Response Headers
#网页内容：有html标签组成的文本
print('<html>')
print('<head>')
print('</head>')
print('<body style="background-color:#eeeeee;">')
print('<pre>')
print('<div style="text-align:center;float:left;height:500px;width:500px;color:green;"> ')
print('<h1 style="">Timesheets 填写个人信息</h1>')
print('<form action="/cgi-bin/response.py" method="post">')
print('QQ            :   <input type="text" name="qq">  <br />')
print('Username      :   <input type="text" name="name">  <br />')
print('Password      :   <input type="text" name="password">  <br />')
print('Job Name      :   <input type="text" name="jobname">  <br />')
print('Description   :   <textarea required="required" name="description" id="description" class="regular-text" rows="4" style="resize: none;width:200;height:120px"></textarea>  <br />')
print('<input type="submit" value="提交" />')
print('</form>')
print('</div>')
print('<div style="float:left;">')
print('<h2>说明：</h2>')
print('     qq号:在qq群发送ts命令的qq号 <br />')
print('     Username:登录http://xxx.xxx.com/的用户名 <br />')
print('     password:登录http://xxx.xxx.com/的密码 <br />')
print('     jobname:填写对应的红色编码 <br />')
print('     description:默认填写description的内容, <br />')
print('</div>')
print('<div style="float:left;font-size:4">')
print('        jobname:对应码 <br />')
print('        <b style="color:red">11</b> , SmartFoundry <br />')
print('        <b style="color:red">22</b> , General Support <br />')
print('        <b style="color:red">23</b> , General Meeting <br />')
print('        <b style="color:red">24</b> , Other management work <br />')
print('        <b style="color:red">27</b> , leave <br />')
print('        <b style="color:red">31</b> , Public Holiday <br />')
print('        <b style="color:red">45</b> , APIBay <br />')
print('        <b style="color:red">46</b> , Pfingo phase3 <br />')
print('        <b style="color:red">48</b> , OTP<br />')
print('        <b style="color:red">50</b> , Toku<br />')
print('</div>')
print('</pre>')
print('</body>')
print('</html>')
