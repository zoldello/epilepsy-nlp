"""
    Papers 
"""
import requests
from Bio import Entrez


class Papers():
    def __init__(self):
        pass


    def get_html(self, *pmids):
        if not pmids:
            return
        ncbi_base_url = 'https://www.ncbi.nlm.nih.gov/pubmed/'
        for pmid in pmids:
            file_pointer = requests.get(''.join([ncbi_base_url, pmid]))
            file_pointer.text
            

    def get_papers_data(self, *pmids):
        '''Returns abstract and full text if available
        
        Arguments:
            pmids {list} -- list of dictionary of full text and abstract
        '''

        #TODO: 
        #(1)Given PMID, get PMCID from page. Then find article on pmcid-page, then scrape. 
        #(2)given pmid, find full text url
        #
        # Is this how you get article: https://stackoverflow.com/questions/37804479/how-to-download-full-article-text-from-pubmed?rq=1?
        #''''
        if not ids:
            print('At least one id is needed')
            return  
        Entrez.email = 'zoldello@gmail.com' #'A.N.Other@example.com' 
        handle = None
        try:
            handle = Entrez.efetch(
                db="pubmed", 
                id= ','.join(pmids),
                rettype='full',
                retmode="xml", 
            ) 
            results = Entrez.read(handle)
        finally:
            if handle:
                handle.close()
        pmcids = []
        for pubmedArticle in results['PubmedArticle']:
            if 'PubmedData' in pubmedArticle and pubmedArticle['PubmedData']['ArticleIdList']:
                        if len(pubmedArticle['PubmedData']['ArticleIdList']) >= 4: 
                            pmcids.append(pubmedArticle['PubmedData']['ArticleIdList'][3].title().upper().strip('PMC')
)
        return pmcids



