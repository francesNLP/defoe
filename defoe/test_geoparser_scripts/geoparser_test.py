import os
import subprocess
import re

#change this according to your path
defoe_path ="/Users/rf208/Research/NLS-Fellowship/work/defoe/"
defoe_path ="/home/rosa_filgueira_vicente/defoe/"
os_type = "sys-i386-64"
# Use the following value for os variable in case you are running this in a MAC
#os_type= "sys-i386-snow-leopard"
gazetteer = "geonames"
bounding_box = ""

def geoparser_cmd(text):
    atempt= 0
    flag = 1
    geoparser_xml = ''
    if "-" in text:
        text=text.replace("-", "")
    if "\\" in text:
        text=text.replace("\\", "")
    if "'" in text:
        text=text.replace("'", "\'\\\'\'")

    print("------ NEW %s\n" %text)
    print("\n")

    cmd = 'echo \'%s\' \''+ text + '\' | '+ defoe_path + 'geoparser-v1.1/scripts/run -t plain -g ' + gazetteer + ' ' + bounding_box + ' -top | ' + defoe_path+ 'georesolve/bin/'+ os_type + '/lxreplace -q s | '+ defoe_path + 'geoparser-v1.1/bin/'+ os_type +'/lxt -s '+ defoe_path+'geoparser-v1.1/lib/georesolve/addfivewsnippet.xsl'
    
    print("CMD is %s" %cmd)

    while (len(geoparser_xml) < 5) and (atempt < 10) and (flag == 1):
        proc=subprocess.Popen(cmd.encode('utf-8'), shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #proc=subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if "Error" in str(stderr):
            flag = 0
            print("err: '{}'".format(stderr))
            print("--------> text is %s" %text)
        else:
            geoparser_xml = stdout
        print(atempt, stdout, stderr)
        atempt+=1
    print("--->Geoparser %s" %geoparser_xml)
    return geoparser_xml

sentence ="I like to live in Madrid, which is the capital of Spain."


#sentence="Wra. Bair Jftltd Wa’tc> Bteir, rob Kei v 18K, Jfoaa Mau Jvew Clytkedule, mtirder, anil Kim On Ross, house Wea King 1818, Nov. A;ex. Itoberfson, hoiif'\''tbreaking nnd tkcft 1819, Ap( Ko Ik M'\''Kinkw, Hunter (juthi , John Borbes, A Win. Ikicir'\''iiint), houstbrvukiiig and theft 3819, Nov. Jo Ish B Rchannu, ttiunier 1819, Noy. 17 Riefnod Sit Mih, bousebreakfng 1820. May'\''ll Jas. Wiiso B, treason (hangt'\''d and beheaded) 1829. Au^, 3 tirant. Peter Crosbie, John Connor, and Tt»0'\''&. M‘Colgi*rr, housfcbi'\''eaidng and robbery 1820, Nor. JS Slj Jung 8 William Leonard Swan, forgery Mii Mni M Hntyro, W dliam Paterson, and James Uyer, li nvsebreaking • . 182 T, Oat.'\'' 24 WH&am C amiibell, bousc-bi an king and theft lft22 v May 39 T hcwims Donn;icliv, do. do. 1822, June £ ,blbn M‘Donald <k Jrmes Wilson, do. do. 1828, Je 4 Pjbivss Cain, robbery, & George Lnidlnw, I Ik-Sc 3 82,8, Oet. ‘j Q David Wylie, housebrenking and theft • 1828, Nov. 12 Wm. M'\''Teague,'\''uttering forged notes 1524 May }.£) J'\''ulm M‘Creevie, housebreaking and-theft lf2 , June 2 Wtl Sittflj Divan, imirder 1824, July 2-1 Jamee Stevensou, highway robbsy l S25 ( Jje 1 J88 Dolko, street robbery 1826, June 7 Audw. Stevraxt & Edward Kelly, stseet robbery 1826, Nov.1 .lamas i.^acs murder 1887, Dee. 12. T. Co QU Oi: & Bell M'\''Menetny, assnnlt & robl^ery, 1S2S, Oct. 22 Thelmas Adkenhead,. for denying the Trinity, &e,, ^•sstx Cufet! at the Gillowlee, on the 8th'\''Jenuary, 1697. Jehu Ogilvie, a Catholic, wss tried in 1615, before tl^'\''Phrtes* Uat Magistrates of Glasgow, for saying of Afetss, See. He was found guilty, and banged that same afternoon ! iuah wa? the hbolaiity of our Protestant ancestors. FOR WITCHCRAFT. Ai CR Parrson, was strangled end>bursed in May, Jmet Grant and Janet C Utk, wore homed in Aagost, The kst person who was brought to the stake m se'\''eotkn*!,’waa tcndeuiaed by pt. David Ross, Sher ff-depate of Surtiertaftd Jn 17C'\''?.Tfefe dawl-hes nover V05 «eea in F8?t ! -.r.d sinye, C2.!a7'\'',8. 0 '\''“f "


geoparser_cmd(sentence)

