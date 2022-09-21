outfile=open("info_security.txt","r")
infile=open("encrypted.txt","w")

encryption=dict(a="1",A="!",b="2",B="@",c="3",C="#",d="4",D="$",e="5",E="%",f="6",F="^",g="7",G="&",h="8",H="*",i="9",I="(",j="0",J=")",k="[",K="{",l="]",L="}",m="|",M=":",n=";",N="'",o='"',O=",",p="D",P="<",q=".",Q=">",r="-",R="_",s="+",S="=",t="?",T="/",u="`",U="~",v="r",V="R",w="e",W="E",x="l",X="L",y="o",Y="O",z="n",Z="N")
read_outfile=outfile.read()
for char in read_outfile:
    if char in encryption:
        infile.write(encryption[char])
    else:
        infile.write(char)

infile.close()
outfile.close()

    