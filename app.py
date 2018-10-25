import spacy
from collections import Counter

from papers import Papers
from epilepsy import Epilepsy



#TO DO/
# Dictionary of gene to count 
# get full text (abstract and body)
# genes synonyms
# !full text
# options to search by text


nlp = spacy.load('en')

if __name__ == '__main__':
    epilepsy = Epilepsy(nlp)
    papers = Papers()
    

    #demos
 
    sample_text = 'APOBEC1CF A2M a2m alpha-1-B glycoprotein 1-aminocyclopropane-1-carboxylate synthase homolog Comprehensive Metabolomics Analysis of Xueshuan Xinmaining Tablet in Blood Stasis Model Rats Using UPLC-Q/TOF-MS.'.upper()
    #print('II')
    #print(f'Synonyms: {epilepsy.synonyms}')
    #print(f'Epilepsy Types: {epilepsy.types}')
    #print(f'Seizure Types: {epilepsy.seizure_types}')
    #print(f'Genes: {epilepsy.genes}')
    #print(f'Raw Genes data: {epilepsy.raw_genes_data}')
    #print(f'Word frequency: {epilepsy.word_frequency(sample_text)}')
    #print(f'All genes and alternate names combined: {epilepsy.flatten_genes_and_alternates_names()}')
    #print(f'Gene count: {epilepsy.gene_to_frequency(sample_text)}')
    #print(f'Gene count: { {i for k,v in epilepsy.gene_to_frequency(sample_text) if v !=0 }')

    for k,v in epilepsy.gene_to_frequency(sample_text).items():
        if (v != 0):
            print(f'Gene: {k}, Count: {v}')

    
    #print(f'Articles: {papers.get_papers_data("21990379", "21658913")}')
    #print(f'{epilepsy.}')
    #print(f'{epilepsy.}')

    #papers.get_papers(['6160742'])
    y = epilepsy.genes #gene_to_frequency(sample_text)
    x = 0
    #-info
    #gene-to-frequency
    #word count

    #gent

    #####
    #search_text = 'alpha-1-B glycoprotein 1-aminocyclopropane-1-carboxylate synthase homolog Comprehensive Metabolomics Analysis of Xueshuan Xinmaining Tablet in Blood Stasis Model Rats Using UPLC-Q/TOF-MS.'
    #epilepsy.word_frequency(search_text)
    #m = epilepsy.epilepsy_and_synonyms_count(search_text)
    #m = epilepsy.gene_to_frequency(search_text)
    #papers.get_papers(['4756107', '17284678', '9998'])
    #####

    #y = 0
    #new_list = [expression(i) for i in old_list if filter(i)]

