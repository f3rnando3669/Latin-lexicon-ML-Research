import pandas as pd
from nltk.corpus import wordnet as wn


# simplifies name, form.v.1 -> form
def simplify_name(name):
    return name.split(".")[0].replace("_", " ")


# list_of_hypernyms --> simplified form of hypernyms, full form of hypernym
def hypernyms_tostring(hypernyms):
    hypernym_simplified = ""
    hypernym_full = ""

    for hypernym in hypernyms:
        name = hypernym.name()
        hypernym_simplified += simplify_name(name)
        hypernym_full += name + " "

    return hypernym_simplified, hypernym_full


# simplifies lemma, Lemma('bruv.n.5') --> bruv
def get_simple_derived(lemma):
    return str(lemma).replace("Lemma('", "").replace("')", "").split(".")[3]


# get full name of a name
def get_full_name(name):
    s_set_of_name = wn.synsets(name)
    full_names = ""
    for s_set in s_set_of_name:
        simp, _ = hypernyms_tostring(s_set.hypernyms())
        full_names += simp + " "

    return full_names


# returns a string with no unnecessary spaces
def filter_cat(name):
    name_list = name.split(" ")
    check = {}
    rv = ""

    for i in range(len(name_list)):
        if not check.__contains__(name_list[i]):
            check[name_list[i]] = ""
            rv += name_list[i] + " "

    return rv


# returns a list of derivationally_related_forms hypernyms
def related_hypernyms(list_of_lemmas):
    cat = ""

    if len(list_of_lemmas) == 0:
        return cat

    unique = set()
    for lemma in list_of_lemmas:
        for derived_form in lemma.derivationally_related_forms():
            simp_derived = get_simple_derived(derived_form)
            if not unique.__contains__(simp_derived):
                cat += (get_full_name(simp_derived))
                unique.add(simp_derived)

    return filter_cat(cat).split(" ")


# get the top level category for a word
# injects a new line in the csv file, for each derivationally_related_forms hypernym
def inject(name, lemma, full_hypernym, lemmas):
    hypernyms = related_hypernyms(lemmas)

    for hypernym in hypernyms:
        if len(hypernym) > 0:
            org_set.append({"word_name": name,
                            "word_hypernym": " ",
                            "word_lemma": lemma,
                            "hypernyms_lemmas": full_hypernym,
                            "categories": hypernym})


title = ["word_name", "word_hypernym", "word_lemma", "hypernyms_lemmas", "categories"]
org_set = []

for syn in wn.all_eng_synsets():
    simple_hypernyms, full_hypernyms, = hypernyms_tostring(syn.hypernyms())

    if len(simple_hypernyms) > 0:
        org_set.append({"word_name": simplify_name(syn.name()),
                        "word_hypernym": simple_hypernyms,
                        "word_lemma": syn.name(),
                        "hypernyms_lemmas": full_hypernyms,
                        "categories": simple_hypernyms})
    else:
        inject(simplify_name(syn.name()), syn.name(), full_hypernyms, syn.lemmas())

df = pd.DataFrame.from_dict(org_set)
df.to_csv(r'wordsandhypernyms.csv', index=False, header=True)
