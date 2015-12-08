#BEGIN_HEADER
from biokbase.workspace.client import Workspace as workspaceService
#END_HEADER


class wjr_count_contigs:
    '''
    Module Name:
    wjr_count_contigs

    Module Description:
    A KBase module: wjr_count_contigs
This sample module contains one small method - count_contigs.
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    #BEGIN_CLASS_HEADER
    workspaceURL = None
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        #END_CONSTRUCTOR
        pass

    def count_contigs(self, ctx, workspace_name, contigset_id):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN count_contigs
        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        contigSet = wsClient.get_objects([{'ref': workspace_name+'/'+contigset_id}])[0]['data']
        provenance = None
        if 'provenance' in ctx:
            provenance = ctx['provenance']
        returnVal = {'contig_count': len(contigSet['contigs']), 'provenance': provenance}
        #END count_contigs

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method count_contigs return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
