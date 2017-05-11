
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import cgi
import xlrd
import xlwt
import xlutils.copy
import os
import re
cgitb.enable()
class info:
    def __init__(self):
        pass
    def getuseinfo_exls(self,qq):
        fname = "F:\\timesheetsinfo.xls"
        bk = xlrd.open_workbook(fname)
        shxrange = range(bk.nsheets)
        try:
            sh = bk.sheet_by_name("Sheet1")
        except:
            print("no sheet in %s named Sheet1",fname)
            return -1
        print("nrows %d, ncols %d" % (sh.nrows,sh.ncols))
        for x in range(1,sh.nrows):
            cell_value = sh.cell_value(x,0)
            # print(int(cell_value))
            if str(int(cell_value)) == qq:
                return x
                # for y in range(1,sh.ncols):
                #     print(sh.cell_value(x,y))
        return -1
    def add_exls(self,body):
        fname = "F:\\timesheetsinfo.xls"
        try:
            bk = xlrd.open_workbook(fname)
            row = bk.sheet_by_name("Sheet1").nrows
            newwb = xlutils.copy.copy(bk)
            sh=newwb.get_sheet(0)
            for x in range(0,len(body)):
                sh.write(row,x,body[x])
            try:
                os.remove(fname)
            except:
                self.send_body("系统正忙，请稍后再试")
            newwb.save(fname)
            self.send_body("添加成功，请在qq群测试")
        except:
            self.send_body("系统错误，请联系唐毅")
    def mod_info(self,row,body):
        fname = "F:\\timesheetsinfo.xls"
        try:
            bk = xlrd.open_workbook(fname)
            newwb = xlutils.copy.copy(bk)
            sh=newwb.get_sheet(0)
            for x in range(0,len(body)):
                sh.write(row,x,body[x])
            try:
                os.remove(fname)
            except:
                self.send_body("系统正忙，请稍后再试")
            newwb.save(fname)
            self.send_body("修改成功，请在qq群测试")
        except:
            self.send_body("系统错误，请联系唐毅")
    def send_head(self):
        print("Content-type:text/html\n")#Response Headers
        #网页内容：有html标签组成的文本
        print('<html>')
        print('<head>')
        print('</head>')
        print('<body style="background-color:#eeeeee;">')
    def send_end(self):
        print('</body>')
        print('</html>')
    def send_body(self,body):
        self.send_head()
        print(body)
        self.send_end()


def main():
    userinfo = info()
    form = cgi.FieldStorage()

    qq = form.getvalue('qq')
    name  = form.getvalue('name')
    password  = form.getvalue('password')
    jobname = form.getvalue('jobname')
    description  = form.getvalue('description')

    vqq = qq.isdigit()
    vjn = jobname.isdigit()
    nbreak = False
    if  vqq== False or vjn == False:
        userinfo.send_head()
        if vqq == False:
            print("qq:",qq,"输入错误<br/>")
        if vjn == False:
            print("jobname:",jobname,"输入错误，请输入对应编码 <br/>")
        print('<a href="/cgi-bin/info.py">返回</a>')
        userinfo.send_end()
        return
    row = userinfo.getuseinfo_exls(qq)
    if row != -1:
        userinfo.mod_info(row,[qq,name,password,jobname,description])
    else:
        userinfo.add_exls([qq,name,password,jobname,description])

main()

