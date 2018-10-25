import spacy
import json

from collections import Counter

class Epilepsy():
    @property
    def synonyms(self):
        '''
        Get Epilepsy Synonyns
        '''
        if not self._synonyms:
            self._synonyms = (
                'epilepsy',
                'epileptic',
                'epileptogenesis',
                'seizure',
                'seize',
                'convulsion',
                'convulse',
                'convulsive',
                'nonconvulsive',
                'non-convulsive',
                'absence seizure',
                'focal seizure',
                'complex partial seizure',
                'status epilepticus',
            )
        return self._synonyms


    @property
    def types(self):
        '''
        Get Epilepsy Types
        '''
        if not self._types:
            self._types = (
                'rolandic',
                'epilepsia partialis continua',
                'Kozhevnikov\'s epilepsia',
                'Kojevnikov\'s epilepsia',
            )       
        return self._types


    @property
    def seizure_types(self):
        '''
        Get seizure types
        '''
        if not self._seizure_types:
            self._seizure_types = (
                'tonic-clonic',
                'tonic',
                'clonic',
                'myoclonic',
                'absence',
                'atonic',
            )
        return self._seizure_types


    @property
    def genes(self):
        '''
        Get human genes' data
        '''
        if not self._raw_genes_data:
            self._raw_genes_data = self._read_gene_json_file()
        return self._raw_genes_data['response']['docs'] 
        

    @property
    def raw_genes_data(self):
        '''
        Get raw human genes' information. Use the property-genes if you do not
        have a strong reason to use this
        '''
        if not self._raw_genes_data:
            self._raw_genes_data = self._read_gene_json_file()
        return self._raw_genes_data
        

    def __init__(self, nlp):
        self.nlp = nlp
        self._synonyms = None
        self._types = None
        self._seizure_types = None
        self._raw_genes_data = None
        self._flatten_gene_name_list = None

    def _read_gene_json_file(self):
        '''Read in the gene json data
        
        Returns:
            dictionary -- Data dump of genes-information
        '''
        with open('genes.json') as genes_json_data:
            genes = json.load(genes_json_data)
        return genes


    def epilepsy_and_synonyms_count(self, text):
        '''Returns count of the word "epilepsy" and synonyms
        
        Arguments:
            text {string} -- Text to count
        
        Returns:
            interger -- word-count
        '''
        if not text:
            print('Cannot do word-frequency analysis on null or empty text')
            return
        word_freq = self.word_frequency(text)
        epilepsy_or_synonym_count = 0
        for epilepsy_or_synonym in self.synonyms:
            word_count = word_freq[epilepsy_or_synonym]
            if word_count == 0:
                continue
            epilepsy_or_synonym_count += word_count
        return epilepsy_or_synonym_count


    def word_frequency(self, text):
        '''Performs a mapping of word to frequency of occurence
        
        Arguments:
            text {string]} -- Text to do word-frequency on
        
        Returns:
            dictionary -- Mapping of word to frequency of occurence
        '''
        if not text:
            print('Cannot do word-frequency analysis on null or empty text')
            return
        doc = self.nlp(u"{}".format(text))
        sanitized_text = [
            token.text for token in doc if not token.is_stop and not token.is_punct and token.pos_ != 'PRON'
            ]
        word_freq = Counter(sanitized_text)
        return word_freq
    

    def flatten_genes_and_alternates_names(self):
        '''Combines name, alias and previous name of all human genes.
        
        Returns:
            list -- List of all human genes combined with alternative names
        '''
        # this is computationally expensive
        if not self._flatten_gene_name_list:
            self._flatten_gene_name_list = []
            # all human gene names and their variants are needed; ordering is irrelevant
            for gene in self.genes:
                self._flatten_gene_name_list.append(gene['symbol'])
                if 'alias_symbol' in gene:
                    self._flatten_gene_name_list.extend([alias_symbol for alias_symbol in gene['alias_symbol']])
                if 'previous_symbol' in gene:
                    self._flatten_gene_name_list.extend([previous_symbol for previous_symbol in gene['previous_symbol']])
        return self._flatten_gene_name_list


    #todo
    # input: pmid 
    # output, list of (pmid,  gene, count, freq)
    # 
    # look at symbol, entrez_id, alias_symbol 
    # gene is based on symbol and alias_symbol or prev_symbol
    #
    # get pmid from pmcid
    def gene_to_frequency(self, text):
        '''Maps gene to frequency of occurence
        
        Arguments:
            text {strinf} -- Text with gene reference
        
        Returns:
            dictionary -- Mapping of gene to frequency
        '''
        if not text:
            print('Cannot do word-frequency analysis on null or empty text')
            return
        genes = self.flatten_genes_and_alternates_names()
        gene_freq = {gene:text.count(gene.strip()) for gene in genes}
        return gene_freq