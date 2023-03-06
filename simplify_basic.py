import re
import subprocess, os

def simp_basic(MMLorg):
    # Removing multiple backslashes
    i = MMLorg.find('\\\\')
    MMLorg = MMLorg.encode().decode('unicode_escape')

    while i >0:
        MMLorg = MMLorg.replace('\\\\', '\\')
        i = MMLorg.find('\\\\')
    
    # Removing initial information about URL, display, and equation itself
    begin = MMLorg.find('<math')+len('<math')
    end = MMLorg.find('>')
    MMLorg = MMLorg.replace(MMLorg[begin:end], '')

    # ATTRIBUTES

    ## Attributes commonly used in MathML codes to represent equations
    elements = ['mrow', 'mi', 'mn', 'mo', 'ms', 'mtext', 'math', 'mtable', 'mspace', 'maction', 'menclose',
                  'merror', 'mfenced', 'mfrac', 'mglyph', 'mlabeledtr', 'mmultiscripts', 'mover', 'mroot',
                  'mpadded', 'mphantom', 'msqrt', 'mstyle', 'msub', 'msubsup', 'msup', 'mtd', 'mtr', 'munder',
                  'munderover', 'semantics']

    ## Attributes that can be removed
    attr_tobe_removed = ['class', 'id', 'style', 'href', 'mathbackground', 'mathcolor']

    ## Attributes that need to be checked before removing, if mentioned in code with their default value,
    ## will be removed else will keep it. This dictionary contains all the attributes with thier default values.
    attr_tobe_checked = {
                        'displaystyle':'false', 'mathsize':'normal', 'mathvariant':'normal','fence':'false',
                        'accent':'false', 'movablelimits':'false', 'largeop':'false', 'stretchy':'false',
                        'lquote':'&quot;', 'rquote':'&quot;', 'overflow':'linebreak', 'display':'block',
                        'denomalign':'center', 'numalign':'center', 'align':'axis', 'rowalign':'baseline',
                        'columnalign':'center', 'alignmentscope':'true', 'equalrows':'true', 'equalcolumns':'true',
                        'groupalign':'{left}', 'linebreak':'auto', 'accentunder':'false'
                       }

    MMLmod = Attribute_Definition(MMLorg, elements, attr_tobe_removed, attr_tobe_checked)

    return MMLmod

def Attribute_Definition(mml_code, elements, attr_tobe_removed, attr_tobe_checked):

    # Defining array to keep Attribute definition
    definition_array = []

    for ele in elements:
        # Getting indices of the position of the element in the MML code
        position = [
            i for i in re.finditer(r"\b%s\b" % re.escape(ele), mml_code)
        ]

        for p in position:
            # Attribute begining and ending indices
            (attr_begin, attr_end) = p.span()

            # length of the definition of the attribute
            length = mml_code[attr_end:].find(">")

            if length > 0:

                # Grabbing definition
                definition = mml_code[attr_end : attr_end + length].split()

                # Append unique definition
                for deftn in definition:
                    if deftn not in definition_array:
                        definition_array.append(deftn)

    # remove all the attributes that need to be removed
    for darr in definition_array:
        if "=" in darr:
            # Attribute and its value -- of the element
            attribute_parameter = darr.replace(" ", "").split("=")[0]
            attribute_value = darr.replace(" ", "").split("=")[1]

            # If Attribute has a defualt value, we can remove it
            # Checking which attributes can be removed
            if attribute_parameter not in attr_tobe_removed:
                if attribute_parameter in attr_tobe_checked.keys():
                    if (
                        attribute_value.replace("\\", "").replace('"', "")
                        == attr_tobe_checked[attribute_parameter]
                    ):
                        mml_code = mml_code.replace(darr, "")
            else:
                mml_code = mml_code.replace(darr, "")

    return mml_code
