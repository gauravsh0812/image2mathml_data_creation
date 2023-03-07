def extract_inbetween_tokens(mml_eqn):
    mmls = [m for m in mml_eqn.split(' ') if m != '']
    mmlss = [m for m in mmls if '<' in m and len([t for t in m if t=='<']) ==2]
    mmls3 = []
    for i in mmlss:
        if '&#x' not in i:
            imml = [im for im in re.split('>|<',i) if im != '']
            print("imml: ", imml)
            if len(imml)>=3 and imml[-1] != '/math':
                if len(imml[1])>1:
                    mmls3.append(imml[1])

    return mmls3


mml = "<math> <mi>l o g</mi> <mi>Z</mi> <mrow> <mo>(</mo> <mi>&#x03B2 </mi> <mo>)</mo> </mrow> <mo>=</mo> <mfrac> <mrow> <mi>f</mi> <mrow> <mo>(</mo> <mn>0</mn> <mo>)</mo> </mrow> </mrow> <mn>2</mn> </mfrac> <mo>&#x2212 </mo> <mi>I</mi> <mrow> <mo>(</mo> <mn>0</mn> <mo>)</mo> </mrow> <mo>&#x2212 </mo> <mn>2</mn> <munderover> <mo>&#x2211 </mo> <mrow > <mi>n</mi> <mo>=</mo> <mn>1</mn> </mrow> <mrow > <mi >&#x221E </mi> </mrow> </munderover> <mi>I</mi> <mrow> <mo>(</mo> <mi>n</mi> <mo>)</mo> </mrow> <mo>,</mo></math>"
extract_inbetween_tokens(mml)
